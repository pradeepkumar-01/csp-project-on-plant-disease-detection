import os
import io
import base64
from collections import Counter
import matplotlib.pyplot as plt

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.core.files.storage import FileSystemStorage

from .forms import UploadForm
from .models import Prediction, UploadHistory
from .utils import predict_image, CLASS_NAMES
from django.conf import settings  # needed for MEDIA paths
from .models import UserProfile
from .gradcam import generate_gradcam


from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login
from django.db.models import Count
from .models import UserProfile, Prediction
from .forms import UserEditForm, ProfileEditForm



def register(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        phone_number = request.POST.get('phone_number', '').strip()
        password1 = request.POST.get('password1', '').strip()
        password2 = request.POST.get('password2', '').strip()

        #  Validation
        if not username or not email or not phone_number or not password1 or not password2:
            messages.error(request, "All fields are required.")
            return render(request, 'detector/register.html', {'plants': PLANTS})

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return render(request, 'detector/register.html', {'plants': PLANTS})

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, 'detector/register.html', {'plants': PLANTS})

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return render(request, 'detector/register.html', {'plants': PLANTS})

        #  Create user
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()

        #  Create linked UserProfile
        UserProfile.objects.create(user=user, phone_number=phone_number)

        #  Auto-login after registration
        login(request, user)
        messages.success(request, "Registration successful! Welcome aboard 🌱")
        return redirect('home')

    #  GET request → show registration page
    return render(request, 'detector/register.html', {'plants': PLANTS})


#  Define this ONCE globally — outside the function
PLANTS = {
    'Grape': ['Leaf_blight_(Isariopsis_Leaf_Spot)', 'Black_rot', 'Esca_(Black_Measles)', 'healthy'],
    'Soybean': ['healthy'],
    'Peach': ['healthy', 'Bacterial_spot'],
    'Tomato': [
        'healthy', 'Tomato_Yellow_Leaf_Curl_Virus', 'Target_Spot', 'Septoria_leaf_spot',
        'Spider_mites_Two-spotted_spider_mite', 'Early_blight', 'Late_blight',
        'Bacterial_spot', 'Tomato_mosaic_virus', 'Leaf_Mold'
    ],
    'Apple': ['Cedar_apple_rust', 'Black_rot', 'Apple_scab', 'healthy'],
    'Pepper,_bell': ['Bacterial_spot', 'healthy'],
    'Cherry_(including_sour)': ['healthy', 'Powdery_mildew'],
    'Strawberry': ['Leaf_scorch', 'healthy'],
    'Corn_(maize)': ['Common_rust_', 'Northern_Leaf_Blight', 'Cercospora_leaf_spot_Gray_leaf_spot', 'healthy'],
    'Potato': ['Late_blight', 'healthy', 'Early_blight'],
    'Blueberry': ['healthy'],
    'Raspberry': ['healthy'],
    'Squash': ['Powdery_mildew'],
    'Orange': ['Haunglongbing_(Citrus_greening)']
}


# 🌿 Home page view
def home(request):
    if request.user.is_authenticated:
        return render(request, 'detector/home_loggedin.html', {'plants': PLANTS})
    else:
        return render(request, 'detector/home.html', {'plants': PLANTS})


# 🌿 Authentication Views
def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'detector/login.html')


def logout_view(request):
    auth_logout(request)
    return redirect('home')


# 🌿 Upload image for prediction
@login_required
def upload_image(request):
    if request.method == "POST" and request.FILES.get("image"):
        uploaded_file = request.FILES["image"]

        # Save uploaded image to MEDIA
        save_path = os.path.join(settings.MEDIA_ROOT, uploaded_file.name)
        with open(save_path, 'wb+') as f:
            for chunk in uploaded_file.chunks():
                f.write(chunk)

        # Predict
        try:
            predicted_class, confidence = predict_image(save_path)
            print(f"[DEBUG] Predicted: {predicted_class}, Confidence: {confidence:.2f}%")
        except Exception as e:
            predicted_class = "Unknown"
            confidence = 0
            print(f"Prediction error: {e}")

        # Extract plant name
        plant_name = predicted_class.split('___')[0] if '___' in predicted_class else predicted_class.split('_')[0]

        # Save prediction to DB
        prediction = Prediction.objects.create(
            user=request.user,
            image=uploaded_file,
            predicted_label=predicted_class,
            confidence=confidence
        )

        # Redirect to the result page for this prediction
        return redirect('result_view', pk=prediction.pk)

    return render(request, "detector/upload.html")

# detector/views.py
@login_required
def result_view(request, pk):
    """Displays the prediction result after image upload."""
    prediction = get_object_or_404(Prediction, pk=pk, user=request.user)

    plant_name = (
        prediction.predicted_label.split('___')[0]
        if '___' in prediction.predicted_label
        else prediction.predicted_label.split('_')[0]
    )

    # Save the uploaded image path for Grad-CAM view
    request.session['image_url'] = prediction.image.url

    context = {
        'image_url': prediction.image.url,
        'predicted_class': prediction.predicted_label,
        'confidence': round(prediction.confidence, 2),
        'plant_name': plant_name,
        'timestamp': prediction.created_at if hasattr(prediction, 'created_at') else None,
    }

    return render(request, 'detector/result.html', context)



@login_required
def layout_view(request):
    """
    Displays Grad-CAM heatmap overlay for the last uploaded leaf image.
    """
    # Default demo images
    original_url = '/static/detector/images/sample_leaf.jpg'
    heatmap_url = '/static/detector/images/sample_heatmap.jpg'

    # Check if the user has uploaded an image
    image_url = request.session.get('image_url', None)
    if image_url and image_url.startswith(settings.MEDIA_URL):
        # Convert MEDIA URL to file path
        relative_path = image_url.replace(settings.MEDIA_URL, '').lstrip('/')
        image_path = os.path.join(settings.MEDIA_ROOT, relative_path)

        # Generate Grad-CAM only if file exists
        if os.path.exists(image_path):
            try:
                heatmap_url = generate_gradcam(image_path)
                original_url = image_url  # keep the original uploaded image
            except Exception as e:
                print(f"Grad-CAM generation failed: {e}")
        else:
            print(f"Uploaded file not found: {image_path}")

    # Debugging info
    print(f"Original Image URL: {original_url}")
    print(f"Heatmap URL: {heatmap_url}")

    context = {
        'image_url': original_url,
        'heatmap_url': heatmap_url,
    }

    return render(request, 'detector/layout.html', context)


# 🌿 Result page
#@login_required
#def result_view(request, pk):
#    prediction = get_object_or_404(Prediction, pk=pk, user=request.user)
#    return render(request, 'detector/result.html', {'prediction': prediction})


# 🌿 History page
@login_required
def history(request):
    user = request.user
    uploads = Prediction.objects.filter(user=user).order_by('-created_at')

    history_data = [
        {
            'id': upload.id,
            'image_url': upload.image.url if upload.image else None,
            'prediction': upload.predicted_label,
            'confidence': round(upload.confidence, 2),
            'timestamp': upload.created_at.strftime("%Y-%m-%d %H:%M"),
        }
        for upload in uploads
    ]

    return render(request, 'detector/history.html', {'history': history_data})


# 🌿 Dashboard (Pie chart)

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Count
from django.contrib.auth.models import User
from .models import Prediction, UploadHistory, DashboardStats

def dashboard_view(request):
    """🌿 Global Dashboard showing all users' statistics and predictions."""
    
    # ✅ Get all predictions
    predictions = Prediction.objects.all()

    # 📊 Compute statistics
    total_users = User.objects.count()
    total_uploads = predictions.count()
    total_diseases_detected = predictions.values('predicted_label').distinct().count()
    avg_confidence = predictions.aggregate(Avg('confidence'))['confidence__avg'] or 0

    # 🌿 Most common disease detected
    most_common = (
        predictions.values('predicted_label')
        .annotate(count=Count('predicted_label'))
        .order_by('-count')
        .first()
    )
    most_common_disease = most_common['predicted_label'] if most_common else "N/A"

    # 📈 Disease distribution data
    disease_data = list(
        predictions.values('predicted_label')
        .annotate(count=Count('predicted_label'))
        .order_by('-count')
    )

    # 🌡 Confidence distribution
    confidence_ranges = {'0–25%': 0, '25–50%': 0, '50–75%': 0, '75–100%': 0}
    for p in predictions:
        if p.confidence < 25:
            confidence_ranges['0–25%'] += 1
        elif p.confidence < 50:
            confidence_ranges['25–50%'] += 1
        elif p.confidence < 75:
            confidence_ranges['50–75%'] += 1
        else:
            confidence_ranges['75–100%'] += 1

    confidence_data = [
        {'range': key, 'count': val} for key, val in confidence_ranges.items()
    ]

    # 🖼 Recent uploads (global)
    recent_uploads = predictions.order_by('-created_at')[:6]

    # 🧾 Update dashboard stats table (optional for admin)
    DashboardStats.objects.update_or_create(
        id=1,
        defaults={
            'total_users': total_users,
            'total_uploads': total_uploads,
            'total_diseases_detected': total_diseases_detected,
        },
    )

    context = {
        'total_users': total_users,
        'total_uploads': total_uploads,
        'total_diseases': total_diseases_detected,
        'avg_confidence': avg_confidence,
        'most_common_disease': most_common_disease,
        'disease_data': disease_data,
        'confidence_data': confidence_data,
        'recent_uploads': recent_uploads,
    }

    return render(request, 'detector/dashboard.html', context)


@login_required
def profile_view(request):
    user = request.user
    profile, _ = UserProfile.objects.get_or_create(user=user)

    # User stats
    total_uploads = Prediction.objects.filter(user=user).count()
    last_upload = Prediction.objects.filter(user=user).order_by('-created_at').first()
    most_common_label = (
        Prediction.objects.filter(user=user)
        .values('predicted_label')
        .annotate(label_count=Count('predicted_label'))
        .order_by('-label_count')
        .first()
    )
    most_common_label = most_common_label['predicted_label'] if most_common_label else '—'

    context = {
        'user': user,
        'profile': profile,
        'total_uploads': total_uploads,
        'last_upload': last_upload,
        'most_common_label': most_common_label,
    }
    return render(request, 'detector/profile.html', context)


@login_required
def edit_profile(request):
    user = request.user
    profile, _ = UserProfile.objects.get_or_create(user=user)

    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=user)
        profile_form = ProfileEditForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, " Profile updated successfully!")
            return redirect('profile')
        else:
            messages.error(request, " Please correct the errors below.")
    else:
        user_form = UserEditForm(instance=user)
        profile_form = ProfileEditForm(instance=profile)

    return render(request, 'detector/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })



def layout_view(request):
    """
    Displays Grad-CAM heatmap overlay for last uploaded leaf image.
    """
    image_url = request.session.get('image_url', None)

    if image_url:
        image_path = os.path.join(settings.MEDIA_ROOT, image_url.replace(settings.MEDIA_URL, '').lstrip('/'))
        heatmap_url = generate_gradcam(image_path)
    else:
        # Demo fallback
        image_url = os.path.join(settings.STATIC_URL, 'detector/images/sample_leaf.jpg')
        heatmap_url = os.path.join(settings.STATIC_URL, 'detector/images/sample_heatmap.jpg')

    context = {
        'image_url': image_url,
        'heatmap_url': heatmap_url,
    }
    print(" IMAGE:", image_url)
    print(" HEATMAP:", heatmap_url)

    return render(request, 'detector/layout.html', context)


from .prevention_data import PLANT_PREVENTIONS
@login_required
def prevention_guide_view(request):
    """Displays prevention guide for plant diseases."""
    return render(request, 'detector/prevention_guide.html', {'plant_preventions': PLANT_PREVENTIONS})


#def result(request, pk):
#    prediction = get_object_or_404(Prediction, pk=pk, user=request.user)
#
#    # Extract plant name (optional formatting)
#    plant_name = prediction.predicted_label.split('___')[0] if '___' in prediction.predicted_label else prediction.predicted_label.split('_')[0]
#
#    return render(request, 'detector/result.html', {
#        'image_url': prediction.image.url,
#        'predicted_class': prediction.predicted_label,
#        'confidence': prediction.confidence,
#        'plant_name': plant_name
#    })



