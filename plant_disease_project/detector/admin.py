from django.contrib import admin
from .models import Prediction, UploadHistory, UserProfile, DashboardStats, LayoutAnalysis


@admin.register(Prediction)
class PredictionAdmin(admin.ModelAdmin):
    list_display = ('user', 'predicted_label', 'confidence', 'created_at')
    search_fields = ('user__username', 'predicted_label')
    list_filter = ('predicted_label', 'created_at')
    ordering = ('-created_at',)


@admin.register(UploadHistory)
class UploadHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'predicted_class', 'confidence', 'timestamp')
    search_fields = ('user__username', 'predicted_class')
    list_filter = ('predicted_class', 'timestamp')
    ordering = ('-timestamp',)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number')
    search_fields = ('user__username', 'phone_number')


@admin.register(DashboardStats)
class DashboardStatsAdmin(admin.ModelAdmin):
    list_display = ('total_users', 'total_uploads', 'total_diseases_detected', 'last_updated')
    readonly_fields = ('last_updated',)
    ordering = ('-last_updated',)


@admin.register(LayoutAnalysis)
class LayoutAnalysisAdmin(admin.ModelAdmin):
    list_display = ('prediction', 'heatmap_image', 'created_at')
    search_fields = ('prediction__predicted_label',)
    ordering = ('-created_at',)
