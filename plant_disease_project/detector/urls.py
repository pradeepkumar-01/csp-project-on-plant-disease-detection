from django.urls import path
from . import views
from detector import views 

urlpatterns = [
    path('', views.home, name='home'),  # 👈 This defines the 'home' URL
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('upload/', views.upload_image, name='upload'),
    path('result/<int:pk>/', views.result_view, name='result_view'),
    path('history/', views.history, name='history'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('profile/', views.profile_view, name='profile'),
    path('layout/', views.layout_view, name='layout'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('prevention_guide/', views.prevention_guide_view, name='prevention_guide'),
]
