"""
Customer Portal APIs - Nhận data từ Admin và gửi data lên Admin
"""
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.utils import timezone
import requests
from django.conf import settings

class CustomerAPIView(viewsets.ViewSet):
    """
    API cho Customer Portal tương tác với Admin
    """
    permission_classes = [AllowAny]  # Cho phép cross-portal access
    
    @action(detail=False, methods=['get'])
    def get_products_from_admin(self, request):
        """Lấy danh sách sản phẩm từ Admin Portal"""
        try:
            admin_api_url = "http://localhost:8000/api/admin-data/products_for_customer/"
            response = requests.get(admin_api_url, timeout=10)
            
            if response.status_code == 200:
                return Response(response.json())
            else:
                return Response({
                    'status': 'error',
                    'message': 'Could not fetch products from admin'
                }, status=status.HTTP_503_SERVICE_UNAVAILABLE)
                
        except requests.exceptions.RequestException as e:
            return Response({
                'status': 'error',
                'message': f'Admin service unavailable: {str(e)}'
            }, status=status.HTTP_503_SERVICE_UNAVAILABLE)
    
    @action(detail=False, methods=['post'])
    def send_order_to_admin(self, request):
        """Gửi đơn hàng lên Admin Portal"""
        try:
            order_data = request.data
            
            # Lưu đơn hàng vào Customer DB trước
            from customer_portal.models import CustomerProfile
            customer = CustomerProfile.objects.get(user=request.user)
            
            # Tạo local order record
            local_order = {
                'customer_id': customer.id,
                'total_amount': order_data.get('total_amount'),
                'delivery_address': order_data.get('delivery_address'),
                'items': order_data.get('items', []),
                'status': 'pending'
            }
            
            # Gửi lên Admin Portal
            admin_api_url = "http://localhost:8000/api/admin-data/receive_customer_order/"
            response = requests.post(admin_api_url, json=local_order, timeout=10)
            
            if response.status_code == 200:
                admin_response = response.json()
                return Response({
                    'status': 'success',
                    'message': 'Order submitted successfully',
                    'admin_order_id': admin_response.get('order_id'),
                    'local_order': local_order
                })
            else:
                return Response({
                    'status': 'error',
                    'message': 'Failed to submit order to admin'
                }, status=status.HTTP_503_SERVICE_UNAVAILABLE)
                
        except Exception as e:
            return Response({
                'status': 'error',
                'message': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

class CustomerInternalAPIView(viewsets.ViewSet):
    """
    Internal APIs cho Admin Portal gọi vào
    """
    permission_classes = [AllowAny]  # Cho phép cross-portal access
    
    @action(detail=False, methods=['get'])
    def stats(self, request):
        """Cung cấp thống kê cho Admin Dashboard"""
        try:
            from customer_portal.models import CustomerProfile
            from django.contrib.auth import get_user_model
            
            User = get_user_model()
            
            stats = {
                'total_customers': CustomerProfile.objects.count(),
                'active_customers': CustomerProfile.objects.filter(is_verified=True).count(),
                'vip_customers': CustomerProfile.objects.filter(is_vip=True).count(),
                'new_customers_this_month': CustomerProfile.objects.filter(
                    created_at__month=timezone.now().month
                ).count(),
            }
            
            return Response({
                'status': 'success',
                'data': stats
            })
        except Exception as e:
            return Response({
                'status': 'error',
                'message': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    @action(detail=False, methods=['post'])
    def sync_customer_data(self, request):
        """Sync dữ liệu customer từ Admin"""
        try:
            customer_data = request.data
            
            from customer_portal.models import CustomerProfile
            from django.contrib.auth import get_user_model
            
            User = get_user_model()
            
            # Tạo hoặc cập nhật customer
            user, created = User.objects.get_or_create(
                username=customer_data.get('username'),
                defaults={
                    'email': customer_data.get('email'),
                    'first_name': customer_data.get('first_name'),
                    'last_name': customer_data.get('last_name'),
                }
            )
            
            profile, created = CustomerProfile.objects.get_or_create(
                user=user,
                defaults={
                    'phone': customer_data.get('phone'),
                    'customer_type': customer_data.get('customer_type', 'individual'),
                    'province': customer_data.get('province', ''),
                    'district': customer_data.get('district', ''),
                    'ward': customer_data.get('ward', ''),
                    'address': customer_data.get('address', ''),
                }
            )
            
            return Response({
                'status': 'success',
                'message': 'Customer data synced successfully',
                'customer_id': profile.id
            })
            
        except Exception as e:
            return Response({
                'status': 'error',
                'message': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

class CustomerNotificationAPIView(viewsets.ViewSet):
    """
    APIs nhận notifications từ các portal khác
    """
    
    @action(detail=False, methods=['post'])
    def new_product(self, request):
        """Nhận thông báo sản phẩm mới từ Admin"""
        try:
            product_id = request.data.get('product_id')
            source = request.data.get('source')
            
            # Tạo notification cho customers
            # Logic để thông báo cho users về sản phẩm mới
            
            return Response({
                'status': 'success',
                'message': 'Product notification received'
            })
        except Exception as e:
            return Response({
                'status': 'error',
                'message': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
