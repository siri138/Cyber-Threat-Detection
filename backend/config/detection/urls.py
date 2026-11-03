from django.urls import path
from .views import detect_threat, dashboard_stats,threat_history

urlpatterns = [
    path('detect/', detect_threat, name='detect-threat'),
    path('dashboard-stats/', dashboard_stats, name='dashboard-stats'),
    path('threat-history/', threat_history, name='threat-history'),
]