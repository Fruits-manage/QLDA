"""
Script tạo 2 đơn hàng test
"""

import os
import sys
import django
from datetime import datetime, date

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fruit_manage.settings')
django.setup()

from products.models import Product, Category, Unit
from companies.models import Company
from orders.models import Order, OrderDetail
from accounts.models import User
from django.contrib.auth import get_user_model

def create_test_orders():
    """Tạo 2 đơn hàng test"""
    print("📋 TẠO 2 ĐƠN HÀNG TEST")
    print("=" * 60)
    
    User = get_user_model()
    
    # Setup test user
    user, created = User.objects.get_or_create(
        username='ordertest2025',
        defaults={
            'email': 'ordertest@example.com',
            'first_name': 'Order',
            'last_name': 'Test',
            'is_staff': True
        }
    )
    if created:
        user.set_password('test123456')
        user.save()
    
    # Tạo dữ liệu cần thiết (sử dụng get_or_create để tránh duplicate)
    category, created = Category.objects.get_or_create(
        name='Trái cây tươi',
        defaults={'description': 'Danh mục trái cây tươi'}
    )
    
    unit_kg, created = Unit.objects.get_or_create(
        name='kg',
        defaults={'description': 'Kilogram'}
    )
    
    unit_thung, created = Unit.objects.get_or_create(
        name='thùng',
        defaults={'description': 'Thùng'}
    )
    
    # Tạo sản phẩm (sử dụng get_or_create)
    product1, created = Product.objects.get_or_create(
        code='APPLE001',
        defaults={
            'name': 'Táo Fuji Nhật Bản',
            'category': category,
            'unit': unit_kg,
            'cost_price': 80000,
            'selling_price': 120000,
            'shelf_life_days': 15,
            'storage_temperature_min': 2,
            'storage_temperature_max': 8,
            'humidity_requirement': 85,
            'hs_code': '080810'
        }
    )
    
    product2, created = Product.objects.get_or_create(
        code='ORANGE001',
        defaults={
            'name': 'Cam sành Việt Nam',
            'category': category,
            'unit': unit_thung,
            'cost_price': 150000,
            'selling_price': 200000,
            'shelf_life_days': 10,
            'storage_temperature_min': 5,
            'storage_temperature_max': 15,
            'humidity_requirement': 80,
            'hs_code': '080520'
        }
    )
    
    product3, created = Product.objects.get_or_create(
        code='GRAPE001',
        defaults={
            'name': 'Nho xanh Úc',
            'category': category,
            'unit': unit_kg,
            'cost_price': 200000,
            'selling_price': 280000,
            'shelf_life_days': 7,
            'storage_temperature_min': 0,
            'storage_temperature_max': 5,
            'humidity_requirement': 90,
            'hs_code': '080610'
        }
    )
    
    # Tạo khách hàng (sử dụng get_or_create)
    customer1, created = Company.objects.get_or_create(
        tax_code='0106123456',
        defaults={
            'name': 'Siêu thị BigC Thăng Long',
            'company_type': 'customer',
            'address': 'Số 222 Trần Duy Hưng, Cầu Giấy, Hà Nội',
            'phone': '0241234567',
            'email': 'bigc.thanglong@email.com',
            'contact_person': 'Nguyễn Văn A',
            'contact_phone': '0912345678',
            'is_active': True
        }
    )
    
    customer2, created = Company.objects.get_or_create(
        tax_code='0106789012',
        defaults={
            'name': 'Cửa hàng trái cây Sạch',
            'company_type': 'customer',
            'address': 'Số 45 Láng Hạ, Đống Đa, Hà Nội',
            'phone': '0247890123',
            'email': 'traicaysach@email.com',
            'contact_person': 'Trần Thị B',
            'contact_phone': '0987654321',
            'is_active': True
        }
    )
    
    try:
        # ĐƠN HÀNG 1
        print("\n🛒 Tạo đơn hàng 1...")
        order1 = Order.objects.create(
            order_type='domestic_sale',
            company=customer1,
            delivery_date=date(2025, 8, 20),
            shipping_address='Số 222 Trần Duy Hưng, Cầu Giấy, Hà Nội',
            payment_status='pending',
            created_by=user
        )
        
        # Chi tiết đơn hàng 1
        detail1_1 = OrderDetail.objects.create(
            order=order1,
            product=product1,  # Táo Fuji
            quantity=50,       # 50kg
            unit_price=120000,
            total_price=50 * 120000  # 6,000,000
        )
        
        detail1_2 = OrderDetail.objects.create(
            order=order1,
            product=product2,  # Cam sành
            quantity=20,       # 20 thùng
            unit_price=200000,
            total_price=20 * 200000  # 4,000,000
        )
        
        # Cập nhật tổng tiền đơn hàng 1
        subtotal1 = detail1_1.total_price + detail1_2.total_price
        order1.subtotal = subtotal1
        order1.discount_amount = 500000  # Giảm 500k
        order1.total_amount = subtotal1 - 500000  # 9,500,000
        order1.save()
        
        print(f"  ✅ Đơn hàng 1: {order1.order_number}")
        print(f"    - Khách hàng: {customer1.name}")
        print(f"    - Sản phẩm: Táo Fuji (50kg), Cam sành (20 thùng)")
        print(f"    - Tổng tiền: {order1.total_amount:,} VND")
        
        # ĐƠN HÀNG 2
        print("\n🛒 Tạo đơn hàng 2...")
        order2 = Order.objects.create(
            order_type='domestic_sale',
            company=customer2,
            delivery_date=date(2025, 8, 25),
            shipping_address='Số 45 Láng Hạ, Đống Đa, Hà Nội',
            payment_status='pending',
            created_by=user
        )
        
        # Chi tiết đơn hàng 2
        detail2_1 = OrderDetail.objects.create(
            order=order2,
            product=product1,  # Táo Fuji
            quantity=30,       # 30kg
            unit_price=120000,
            total_price=30 * 120000  # 3,600,000
        )
        
        detail2_2 = OrderDetail.objects.create(
            order=order2,
            product=product3,  # Nho xanh
            quantity=15,       # 15kg
            unit_price=280000,
            total_price=15 * 280000  # 4,200,000
        )
        
        # Cập nhật tổng tiền đơn hàng 2
        subtotal2 = detail2_1.total_price + detail2_2.total_price
        order2.subtotal = subtotal2
        order2.discount_amount = 0  # Không giảm giá
        order2.total_amount = subtotal2  # 7,800,000
        order2.save()
        
        print(f"  ✅ Đơn hàng 2: {order2.order_number}")
        print(f"    - Khách hàng: {customer2.name}")
        print(f"    - Sản phẩm: Táo Fuji (30kg), Nho xanh (15kg)")
        print(f"    - Tổng tiền: {order2.total_amount:,} VND")
        
        print("\n" + "=" * 60)
        print("🎉 TẠO 2 ĐƠN HÀNG THÀNH CÔNG!")
        print(f"📊 Tổng giá trị 2 đơn hàng: {(order1.total_amount + order2.total_amount):,} VND")
        
        print("\n📋 CHI TIẾT ĐƠN HÀNG:")
        print(f"Đơn hàng 1 ({order1.order_number}):")
        print(f"  - {detail1_1.product.name}: {detail1_1.quantity} {detail1_1.product.unit.name} x {detail1_1.unit_price:,} = {detail1_1.total_price:,}")
        print(f"  - {detail1_2.product.name}: {detail1_2.quantity} {detail1_2.product.unit.name} x {detail1_2.unit_price:,} = {detail1_2.total_price:,}")
        print(f"  - Giảm giá: {order1.discount_amount:,}")
        print(f"  - Thành tiền: {order1.total_amount:,}")
        
        print(f"\nĐơn hàng 2 ({order2.order_number}):")
        print(f"  - {detail2_1.product.name}: {detail2_1.quantity} {detail2_1.product.unit.name} x {detail2_1.unit_price:,} = {detail2_1.total_price:,}")
        print(f"  - {detail2_2.product.name}: {detail2_2.quantity} {detail2_2.product.unit.name} x {detail2_2.unit_price:,} = {detail2_2.total_price:,}")
        print(f"  - Giảm giá: {order2.discount_amount:,}")
        print(f"  - Thành tiền: {order2.total_amount:,}")
        
        print("\n🔗 XEM ĐƠN HÀNG:")
        print(f"http://127.0.0.1:8000/orders/{order1.id}/")
        print(f"http://127.0.0.1:8000/orders/{order2.id}/")
        
    except Exception as e:
        print(f"❌ Lỗi tạo đơn hàng: {str(e)}")
        # Cleanup nếu có lỗi
        if 'order1' in locals():
            order1.delete()
        if 'order2' in locals():
            order2.delete()
    
    # Không cleanup để có thể xem đơn hàng
    print(f"\n💡 Test user: {user.username} / test123456")

if __name__ == '__main__':
    create_test_orders()
