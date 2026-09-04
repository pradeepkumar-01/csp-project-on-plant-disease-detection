import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import transforms
import numpy as np
import cv2
from PIL import Image
import os
from django.conf import settings
import json

# ✅ Use your trained ResNet9 definition
class ResNet9(nn.Module):
    def __init__(self, in_channels, num_classes):
        super().__init__()
        self.conv1 = nn.Sequential(
            nn.Conv2d(in_channels, 64, 3, 1, 1),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.MaxPool2d(2, 2)
        )
        self.conv2 = nn.Sequential(
            nn.Conv2d(64, 128, 3, 1, 1),
            nn.BatchNorm2d(128),
            nn.ReLU(),
            nn.MaxPool2d(2, 2)
        )
        self.res1 = nn.Sequential(
            nn.Conv2d(128, 128, 3, 1, 1),
            nn.BatchNorm2d(128),
            nn.ReLU()
        )
        self.conv3 = nn.Sequential(
            nn.Conv2d(128, 256, 3, 1, 1),
            nn.BatchNorm2d(256),
            nn.ReLU(),
            nn.MaxPool2d(2, 2)
        )
        self.res2 = nn.Sequential(
            nn.Conv2d(256, 256, 3, 1, 1),
            nn.BatchNorm2d(256),
            nn.ReLU()
        )
        self.classifier = nn.Sequential(
            nn.AdaptiveAvgPool2d(1),
            nn.Flatten(),
            nn.Linear(256, num_classes)
        )

    def forward(self, xb):
        out = self.conv1(xb)
        out = self.conv2(out)
        out = out + self.res1(out)
        out = self.conv3(out)
        out = out + self.res2(out)
        out = self.classifier(out)
        return out


def generate_gradcam(image_path):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model_path = os.path.join(settings.BASE_DIR, "plant_disease_model_final.pth")
    class_path = os.path.join(settings.BASE_DIR, "class_names.json")

    # Load class names
    import json
    with open(class_path, "r") as f:
        CLASS_NAMES = json.load(f)

    # Load model
    model = ResNet9(3, len(CLASS_NAMES)).to(device)
    model.load_state_dict(torch.load(model_path, map_location=device))
    model.eval()

    # Target layer
    target_layer = model.res2  # last conv block

    # Preprocess
    transform = transforms.Compose([
        transforms.Resize((256, 256)),
        transforms.ToTensor()
    ])
    img = Image.open(image_path).convert("RGB")
    input_tensor = transform(img).unsqueeze(0).to(device)

    activations = []
    gradients = []

    def forward_hook(module, input, output):
        activations.append(output)

    def backward_hook(module, grad_in, grad_out):
        gradients.append(grad_out[0])

    handle_f = target_layer.register_forward_hook(forward_hook)
    handle_b = target_layer.register_backward_hook(backward_hook)

    output = model(input_tensor)
    pred_class = output.argmax(dim=1).item()
    output[:, pred_class].backward()

    handle_f.remove()
    handle_b.remove()

    grad = gradients[0].cpu().data.numpy()[0]
    act = activations[0].cpu().data.numpy()[0]

    weights = np.mean(grad, axis=(1, 2))
    cam = np.zeros(act.shape[1:], dtype=np.float32)
    for i, w in enumerate(weights):
        cam += w * act[i]

    cam = np.maximum(cam, 0)
    cam = cv2.resize(cam, (256, 256), interpolation=cv2.INTER_LINEAR)
    cam = cam - np.min(cam)
    cam = cam / (np.max(cam) + 1e-8)

    heatmap = cv2.applyColorMap(np.uint8(255 * cam), cv2.COLORMAP_JET)
    img_cv = cv2.cvtColor(np.array(img.resize((256, 256))), cv2.COLOR_RGB2BGR)
    overlay = np.uint8(0.5 * heatmap + 0.5 * img_cv)

    output_dir = os.path.join(settings.BASE_DIR, "detector", "static", "detector", "images")
    os.makedirs(output_dir, exist_ok=True)
    heatmap_path = os.path.join(output_dir, "sample_heatmap.jpg")
    cv2.imwrite(heatmap_path, overlay)

    return  "/static/detector/images/sample_heatmap.jpg"
