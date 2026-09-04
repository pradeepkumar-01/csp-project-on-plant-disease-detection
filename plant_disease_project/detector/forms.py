from django import forms
from .models import Prediction
from .models import UserProfile
from django.contrib.auth.models import User

class UploadForm(forms.ModelForm):
    class Meta:
        model = Prediction
        fields = ['image']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone_number', 'bio', 'profile_pic']

