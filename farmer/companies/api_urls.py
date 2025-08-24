"""
URL Configuration for Farmer Portal APIs
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from companies.api_views import FarmerAPIView, FarmerInternalAPIView, FarmerNotificationAPIView

router = DefaultRouter()
router.register(r'farmer', FarmerAPIView, basename='farmer')
router.register(r'internal', FarmerInternalAPIView, basename='internal')
router.register(r'notifications', FarmerNotificationAPIView, basename='notifications')

urlpatterns = [
    path('api/', include(router.urls)),
]
