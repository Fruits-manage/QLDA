"""
URL configuration for fruit_manage project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('accounts/', include('accounts.urls')),  # Bao gồm FarmerProfile
    # path('companies/', include('companies.urls')),  # Xóa - không cần companies
    path('products/', include('products.urls')),    # Farmer đăng ký sản phẩm
    path('inventory/', include('inventory.urls')),
    path('orders/', include('orders.urls')),        # Farmer nhận đơn hàng
    path('payments/', include('payments.urls')),
    # path('import-export/', include('import_export.urls')),  # Farmer không cần import-export
    path('news/', include('news.urls')),
    # path('activity-logs/', include('activity_logs.urls')),  # Farmer không cần activity logs
    # path('management/', include('management.urls')),        # Farmer không cần management
    path('api/', include('utils.api_urls')),
    # path('', include('companies.api_urls')),  # Xóa - API sẽ từ accounts
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
