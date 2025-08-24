from django.urls import path, include
from rest_framework.routers import DefaultRouter
from utils.api_views import FarmerAPIView, FarmerInternalAPIView

router = DefaultRouter()
router.register(r'farmer', FarmerAPIView, basename='farmer')
router.register(r'internal', FarmerInternalAPIView, basename='internal')

urlpatterns = [
    path('auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
]
