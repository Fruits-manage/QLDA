"""
Farmer Portal APIs - Nhận data từ Admin và gửi data lên Admin
"""
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
import requests
from django.utils import timezone

class FarmerAPIView(viewsets.ViewSet):
    """
    API cho Farmer Portal tương tác với Admin
    """
    
    @action(detail=False, methods=['get'])
    def get_orders_from_admin(self, request):
        """Lấy danh sách đơn hàng từ Admin Portal"""
        try:
            # Lấy farmer_id từ user hiện tại
            from companies.models import FarmerProfile
            farmer = FarmerProfile.objects.get(user=request.user)
            
            admin_api_url = f"http://localhost:8000/api/admin-data/orders_for_farmer/?farmer_id={farmer.id}"
            response = requests.get(admin_api_url, timeout=10)
            
            if response.status_code == 200:
                return Response(response.json())
            else:
                return Response({
                    'status': 'error',
                    'message': 'Could not fetch orders from admin'
                }, status=status.HTTP_503_SERVICE_UNAVAILABLE)
                
        except requests.exceptions.RequestException as e:
            return Response({
                'status': 'error',
                'message': f'Admin service unavailable: {str(e)}'
            }, status=status.HTTP_503_SERVICE_UNAVAILABLE)
        except Exception as e:
            return Response({
                'status': 'error',
                'message': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['post'])
    def send_product_to_admin(self, request):
        """Gửi thông tin sản phẩm lên Admin Portal"""
        try:
            product_data = request.data
            
            # Lưu sản phẩm vào Farmer DB trước
            from companies.models import FarmerProfile, CropProduct
            farmer = FarmerProfile.objects.get(user=request.user)
            
            # Tạo local product record
            local_product = CropProduct.objects.create(
                farmer=farmer,
                product_name=product_data.get('name'),
                variety=product_data.get('variety'),
                price_per_kg=product_data.get('price'),
                expected_yield=product_data.get('quantity'),
                description=product_data.get('description'),
                status='available'
            )
            
            # Chuẩn bị data để gửi lên Admin
            admin_product_data = {
                'farmer_id': farmer.id,
                'name': product_data.get('name'),
                'price': product_data.get('price'),
                'description': product_data.get('description'),
                'variety': product_data.get('variety'),
                'quantity': product_data.get('quantity'),
                'farmer_product_id': local_product.id
            }
            
            # Gửi lên Admin Portal
            admin_api_url = "http://localhost:8000/api/admin-data/receive_farmer_product/"
            response = requests.post(admin_api_url, json=admin_product_data, timeout=10)
            
            if response.status_code == 200:
                admin_response = response.json()
                return Response({
                    'status': 'success',
                    'message': 'Product submitted successfully',
                    'admin_product_id': admin_response.get('product_id'),
                    'local_product_id': local_product.id
                })
            else:
                # Xóa local product nếu không gửi được lên admin
                local_product.delete()
                return Response({
                    'status': 'error',
                    'message': 'Failed to submit product to admin'
                }, status=status.HTTP_503_SERVICE_UNAVAILABLE)
                
        except Exception as e:
            return Response({
                'status': 'error',
                'message': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['post'])
    def update_order_status(self, request):
        """Cập nhật trạng thái đơn hàng"""
        try:
            order_id = request.data.get('order_id')
            new_status = request.data.get('status')
            
            # Gửi cập nhật lên Admin Portal
            admin_api_url = f"http://localhost:8000/api/admin-data/update_order_status/"
            data = {
                'order_id': order_id,
                'status': new_status,
                'updated_by': 'farmer',
                'farmer_id': request.user.farmer_profile.id
            }
            
            response = requests.post(admin_api_url, json=data, timeout=10)
            
            if response.status_code == 200:
                return Response({
                    'status': 'success',
                    'message': 'Order status updated successfully'
                })
            else:
                return Response({
                    'status': 'error',
                    'message': 'Failed to update order status'
                }, status=status.HTTP_503_SERVICE_UNAVAILABLE)
                
        except Exception as e:
            return Response({
                'status': 'error',
                'message': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

class FarmerInternalAPIView(viewsets.ViewSet):
    """
    Internal APIs cho Admin Portal gọi vào
    """
    
    @action(detail=False, methods=['get'])
    def stats(self, request):
        """Cung cấp thống kê cho Admin Dashboard"""
        try:
            from companies.models import FarmerProfile, CropProduct
            
            stats = {
                'total_farmers': FarmerProfile.objects.count(),
                'active_farmers': FarmerProfile.objects.filter(is_active=True).count(),
                'verified_farmers': FarmerProfile.objects.filter(is_verified=True).count(),
                'total_products': CropProduct.objects.count(),
                'available_products': CropProduct.objects.filter(status='available').count(),
                'total_farm_area': FarmerProfile.objects.aggregate(
                    total=models.Sum('total_farm_area')
                )['total'] or 0,
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
    def sync_farmer_data(self, request):
        """Sync dữ liệu farmer từ Admin"""
        try:
            farmer_data = request.data
            
            from companies.models import FarmerProfile
            from accounts.models import User
            
            # Tạo hoặc cập nhật farmer
            user, created = User.objects.get_or_create(
                username=farmer_data.get('username'),
                defaults={
                    'email': farmer_data.get('email'),
                    'first_name': farmer_data.get('first_name'),
                    'last_name': farmer_data.get('last_name'),
                    'role': 'staff'
                }
            )
            
            profile, created = FarmerProfile.objects.get_or_create(
                user=user,
                defaults={
                    'phone': farmer_data.get('phone'),
                    'farmer_type': farmer_data.get('farmer_type', 'individual'),
                    'province': farmer_data.get('province', ''),
                    'district': farmer_data.get('district', ''),
                    'ward': farmer_data.get('ward', ''),
                    'address': farmer_data.get('address', ''),
                    'total_farm_area': farmer_data.get('total_farm_area', 0),
                    'main_crops': farmer_data.get('main_crops', ''),
                }
            )
            
            return Response({
                'status': 'success',
                'message': 'Farmer data synced successfully',
                'farmer_id': profile.id
            })
            
        except Exception as e:
            return Response({
                'status': 'error',
                'message': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

class FarmerNotificationAPIView(viewsets.ViewSet):
    """
    APIs nhận notifications từ các portal khác
    """
    
    @action(detail=False, methods=['post'])
    def new_order(self, request):
        """Nhận thông báo đơn hàng mới từ Admin"""
        try:
            order_id = request.data.get('order_id')
            farmer_id = request.data.get('farmer_id')
            source = request.data.get('source')
            
            # Tạo notification cho farmer
            # Logic để thông báo cho farmer về đơn hàng mới
            
            return Response({
                'status': 'success',
                'message': 'Order notification received'
            })
        except Exception as e:
            return Response({
                'status': 'error',
                'message': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
