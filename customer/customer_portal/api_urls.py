"""
URL Configuration for Customer Portal APIs
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from customer_portal.api_views import CustomerAPIView, CustomerInternalAPIView, CustomerNotificationAPIView

router = DefaultRouter()
router.register(r'customer', CustomerAPIView, basename='customer')
router.register(r'internal', CustomerInternalAPIView, basename='internal')
router.register(r'notifications', CustomerNotificationAPIView, basename='notifications')

urlpatterns = [
    path('api/', include(router.urls)),
]
