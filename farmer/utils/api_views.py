"""
Farmer Portal APIs - Cung cấp thông tin farmer và nhận data từ Admin
"""
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.http import JsonResponse
import requests
from django.conf import settings

class FarmerAPIView(viewsets.ViewSet):
    """
    API của Farmer Portal để giao tiếp với Admin
    """
    permission_classes = [AllowAny]  # Cho phép cross-portal access
    
    @action(detail=False, methods=['get'])
    def get_orders_from_admin(self, request):
        """Lấy danh sách đơn hàng từ Admin Portal"""
        try:
            # Gọi API từ Admin Portal
            admin_url = "http://localhost:8000/api/admin-data/orders_for_farmer/"
            response = requests.get(admin_url, timeout=10)
            
            if response.status_code == 200:
                return Response({
                    'success': True,
                    'data': response.json(),
                    'message': 'Successfully fetched orders from admin'
                })
            else:
                return Response({
                    'success': False,
                    'message': f'Failed to fetch orders from admin: {response.status_code}'
                }, status=response.status_code)
                
        except requests.exceptions.RequestException as e:
            return Response({
                'success': False,
                'message': f'Connection error to admin portal: {str(e)}'
            }, status=status.HTTP_503_SERVICE_UNAVAILABLE)
    
    @action(detail=False, methods=['post'])
    def send_products_to_admin(self, request):
        """Gửi sản phẩm mới lên Admin Portal"""
        try:
            from products.models import Product
            from accounts.models import FarmerProfile
            
            # Lấy thông tin farmer hiện tại
            if not request.user.is_authenticated:
                return Response({
                    'success': False,
                    'message': 'Authentication required'
                }, status=status.HTTP_401_UNAUTHORIZED)
            
            try:
                farmer_profile = request.user.farmer_profile
            except:
                return Response({
                    'success': False,
                    'message': 'Farmer profile not found'
                }, status=status.HTTP_404_NOT_FOUND)
            
            # Lấy danh sách sản phẩm của farmer
            products = Product.objects.filter(created_by=request.user)
            
            product_data = []
            for product in products:
                product_data.append({
                    'name': product.name,
                    'price': str(product.price),
                    'description': product.description,
                    'farmer_name': farmer_profile.farm_name,
                    'farmer_code': farmer_profile.farmer_code,
                    'available_quantity': getattr(product, 'stock_quantity', 0),
                })
            
            # Gửi lên Admin Portal
            admin_url = "http://localhost:8000/api/admin-data/receive_farmer_product/"
            payload = {
                'farmer_id': farmer_profile.id,
                'products': product_data
            }
            
            response = requests.post(admin_url, json=payload, timeout=10)
            
            if response.status_code == 200:
                return Response({
                    'success': True,
                    'message': 'Products sent to admin successfully',
                    'data': response.json()
                })
            else:
                return Response({
                    'success': False,
                    'message': f'Failed to send products to admin: {response.status_code}'
                }, status=response.status_code)
                
        except Exception as e:
            return Response({
                'success': False,
                'message': f'Error: {str(e)}'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class FarmerInternalAPIView(viewsets.ViewSet):
    """
    API nội bộ cho Admin Portal truy cập thông tin Farmer
    """
    permission_classes = [AllowAny]  # Cho phép cross-portal access
    
    @action(detail=False, methods=['get'])
    def stats(self, request):
        """Thống kê cho Admin Dashboard"""
        try:
            from accounts.models import FarmerProfile
            from products.models import Product
            from orders.models import Order
            
            total_farmers = FarmerProfile.objects.count()
            active_farmers = FarmerProfile.objects.filter(is_active=True).count()
            total_products = Product.objects.count()
            pending_orders = Order.objects.filter(status='pending').count()
            
            return Response({
                'success': True,
                'data': {
                    'total_farmers': total_farmers,
                    'active_farmers': active_farmers,
                    'total_products': total_products,
                    'pending_orders': pending_orders,
                }
            })
            
        except Exception as e:
            return Response({
                'success': False,
                'message': f'Error: {str(e)}'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
