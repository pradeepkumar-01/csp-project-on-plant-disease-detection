# 🌿 Plant Disease Detection System (CSP Project)

An intelligent deep learning web application built with **Django** and **PyTorch (ResNet9)** that detects 38 different plant leaf diseases with visual explainability powered by **Grad-CAM** heatmaps and provides actionable prevention guides.

---

## 📌 Features

- 🔬 **Accurate Disease Detection**: Identifies healthy and diseased conditions across 14 crop species (38 classes) using a custom ResNet-9 deep learning model.
- 🔍 **Grad-CAM Explainable AI**: Visualizes model attention through heatmaps to show exactly which leaf areas contributed to the diagnosis.
- 🛡️ **Prevention & Treatment Guide**: Comprehensive recommendations and organic/chemical remedies for detected plant diseases.
- 📊 **Interactive Analytics Dashboard**: Live statistics showing disease distribution, diagnosis activity, and recent predictions.
- 📁 **Prediction History**: Logged history of uploaded leaves and diagnosis results for registered users.
- 👤 **User Authentication & Profile**: Secure login, registration, and user profile management.

---

## 🌾 Supported Crops & Diseases (38 Classes)

Covers 14 crops including **Apple, Blueberry, Cherry, Corn (Maize), Grape, Orange, Peach, Bell Pepper, Potato, Raspberry, Soybean, Squash, Strawberry, and Tomato**.

- **Apple**: Apple Scab, Black Rot, Cedar Apple Rust, Healthy
- **Corn**: Common Rust, Gray Leaf Spot, Northern Leaf Blight, Healthy
- **Grape**: Black Rot, Esca (Black Measles), Leaf Blight, Healthy
- **Potato**: Early Blight, Late Blight, Healthy
- **Tomato**: Bacterial Spot, Early Blight, Late Blight, Leaf Mold, Septoria Leaf Spot, Spider Mites, Target Spot, Yellow Leaf Curl Virus, Mosaic Virus, Healthy
- *...and more.*

---

## 🛠️ Tech Stack

- **Backend**: Django 5.x, Python
- **Deep Learning**: PyTorch, Torchvision (ResNet-9 Architecture)
- **Computer Vision**: OpenCV, Pillow, Grad-CAM
- **Data Visualization**: Matplotlib, Chart.js
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/MANIDEEP-24091a05cg/csp-project-on-plant-disease-detection.git
cd csp-project-on-plant-disease-detection
```

### 2. Create and Activate Virtual Environment
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux / macOS
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Migrations & Start Server
```bash
cd plant_disease_project
python manage.py migrate
python manage.py runserver
```

Open your browser and navigate to `http://127.0.0.1:8000/`.

---

## 📂 Project Structure

```
csp-project-on-plant-disease-detection/
├── plant_disease_project/              # Main Django project directory
│   ├── manage.py                       # Django management utility
│   ├── class_names.json                # 38 plant disease class labels
│   ├── plant_disease_model.pth         # PyTorch trained model weights
│   ├── plant_disease_model_final.pth   # Final PyTorch model weights
│   ├── detector/                       # Detection app
│   │   ├── admin.py
│   │   ├── forms.py
│   │   ├── gradcam.py                  # Grad-CAM heatmap generator
│   │   ├── models.py                   # Prediction & profile models
│   │   ├── prevention_data.py          # Plant prevention tips
│   │   ├── resnet9.py                  # ResNet9 CNN architecture
│   │   ├── urls.py
│   │   ├── utils.py                    # Inference utilities
│   │   ├── views.py                    # Views & dashboard logic
│   │   ├── templates/                  # HTML templates
│   │   └── static/                     # CSS, JS, and image assets
│   ├── media/                          # Uploaded samples & history
│   └── plant_disease_project/          # Project configuration (settings, urls, wsgi)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 👥 Author
- **Manideep Bingimalla**
- GitHub: [@MANIDEEP-24091a05cg](https://github.com/MANIDEEP-24091a05cg)