import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import transforms
from PIL import Image
import json
import os
from django.conf import settings

# 1️⃣ Model definition
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


# 2️⃣ Load class names
class_path = os.path.join(settings.BASE_DIR, "class_names.json")
with open(class_path, "r") as f:
    CLASS_NAMES = json.load(f)

# 3️⃣ Load model
model_path = os.path.join(settings.BASE_DIR, "plant_disease_model_final.pth")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = ResNet9(3, len(CLASS_NAMES)).to(device)
model.load_state_dict(torch.load(model_path, map_location=device))
model.eval()

# 4️⃣ Transform
transform = transforms.Compose([
    transforms.Resize((256, 256)),
    transforms.ToTensor()
])

# 5️⃣ Predict
def predict_image(image_path):
    img = Image.open(image_path).convert("RGB")
    img_tensor = transform(img).unsqueeze(0).to(device)

    with torch.no_grad():
        outputs = model(img_tensor)
        probs = F.softmax(outputs, dim=1)
        conf, pred_idx = torch.max(probs, 1)

    label = CLASS_NAMES[pred_idx.item()]
    confidence = conf.item() * 100
    return label, confidence
