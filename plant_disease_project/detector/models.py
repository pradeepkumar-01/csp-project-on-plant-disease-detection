# plantapp/models.py

from django.db import models
from django.contrib.auth.models import User

# =============================
# Prediction & History Models
# =============================

class Prediction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/')
    predicted_label = models.CharField(max_length=100)
    confidence = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.predicted_label}"


class UploadHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='history/')
    predicted_class = models.CharField(max_length=100)
    confidence = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.predicted_class}"


# =============================
# User Profile Model
# =============================

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profiles/', default='profiles/default.png', blank=True)

    def __str__(self):
        return self.user.username


# =============================
# Dashboard Statistics Model
# =============================

class DashboardStats(models.Model):
    """Tracks overall system usage for admin dashboard."""
    total_users = models.IntegerField(default=0)
    total_uploads = models.IntegerField(default=0)
    total_diseases_detected = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Dashboard Stats ({self.last_updated.strftime('%Y-%m-%d %H:%M')})"


# =============================
# Grad-CAM / Layout Analysis
# =============================

class LayoutAnalysis(models.Model):
    """Stores visualization data for highlighting leaf regions used in prediction."""
    prediction = models.ForeignKey(Prediction, on_delete=models.CASCADE)
    heatmap_image = models.ImageField(upload_to='layout_heatmaps/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Layout for {self.prediction.predicted_label}"

