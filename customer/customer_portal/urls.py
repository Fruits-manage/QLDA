from django.urls import path
from . import views

app_name = 'customer_portal'

urlpatterns = [
    path('', views.CustomerHomeView.as_view(), name='home'),
    path('products/', views.ProductListView.as_view(), name='product_list'),
]
