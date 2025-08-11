"""
Test script để test tất cả chức năng cần thiết
"""

import os
import sys
import django
import requests
from datetime import datetime, date

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fruit_manage.settings')
django.setup()

from products.models import Product, Category, Unit
from companies.models import Company
from orders.models import Order, OrderDetail
from inventory.models import Warehouse, InventoryStock, StockMovement
from accounts.models import User
from news.models import News
from django.contrib.auth import get_user_model

def test_functionality():
    """Test các chức năng chính"""
    print("🧪 COMPREHENSIVE FUNCTIONALITY TEST")
    print("=" * 80)
    
    User = get_user_model()
    
    # Setup test user
    user, created = User.objects.get_or_create(
        username='testuser2025',
        defaults={
            'email': 'test2025@example.com',
            'first_name': 'Test',
            'last_name': 'User 2025',
            'is_staff': True,
            'is_superuser': True
        }
    )
    if created:
        user.set_password('test123456')
        user.save()
    
    results = []
    
    # Test 1: Tạo đơn hàng
    print("\n📋 Test 1: Tạo đơn hàng...")
    try:
        # Tạo dữ liệu cần thiết
        category = Category.objects.create(
            name='Test Category Order',
            description='Test for order'
        )
        
        unit = Unit.objects.create(
            name='test_unit_order',
            description='Test Unit for Order'
        )
        
        product = Product.objects.create(
            code='TESTORDER001',
            name='Test Product for Order',
            category=category,
            unit=unit,
            cost_price=2000,
            selling_price=3000,
            shelf_life_days=10,
            storage_temperature_min=5,
            storage_temperature_max=25,
            humidity_requirement=80,
            hs_code='123456'
        )
        
        company = Company.objects.create(
            name='Test Company Order',
            company_type='limited',
            tax_code='TESTORDER123',
            is_active=True
        )
        
        # Tạo đơn hàng
        order = Order.objects.create(
            order_type='domestic_sale',
            company=company,
            delivery_date=date(2025, 9, 15),
            shipping_address='Test Order Address',
            payment_status='pending',
            created_by=user
        )
        
        # Tạo chi tiết đơn hàng
        order_detail = OrderDetail.objects.create(
            order=order,
            product=product,
            quantity=10,
            unit_price=3000,
            total_price=30000
        )
        
        # Cập nhật tổng tiền
        order.subtotal = 30000
        order.discount_amount = 0
        order.total_amount = 30000
        order.save()
        
        print(f"  ✅ Đơn hàng tạo thành công: {order.order_number}")
        print(f"    - Khách hàng: {company.name}")
        print(f"    - Sản phẩm: {product.name} x {order_detail.quantity}")
        print(f"    - Tổng tiền: {order.total_amount:,} VND")
        results.append(("Tạo đơn hàng", True))
        
        # Cleanup
        order_detail.delete()
        order.delete()
        company.delete()
        product.delete()
        category.delete()
        unit.delete()
        
    except Exception as e:
        print(f"  ❌ Tạo đơn hàng thất bại: {str(e)}")
        results.append(("Tạo đơn hàng", False))
    
    # Test 2: Thêm kho mới
    print("\n🏪 Test 2: Thêm kho mới...")
    try:
        import random
        random_num = random.randint(10000, 99999)
        
        warehouse = Warehouse.objects.create(
            name=f'Kho Test {random_num}',
            code=f'KHO{random_num}',
            address=f'Địa chỉ kho test {random_num}',
            capacity=5000.00,
            manager=user,
            is_active=True
        )
        
        print(f"  ✅ Kho tạo thành công: {warehouse.name}")
        print(f"    - Mã kho: {warehouse.code}")
        print(f"    - Sức chứa: {warehouse.capacity} tấn")
        print(f"    - Quản lý: {warehouse.manager.get_full_name()}")
        results.append(("Thêm kho mới", True))
        
        warehouse.delete()
        
    except Exception as e:
        print(f"  ❌ Thêm kho mới thất bại: {str(e)}")
        results.append(("Thêm kho mới", False))
    
    # Test 3: Tạo biến động kho
    print("\n📦 Test 3: Tạo biến động kho...")
    try:
        import random
        random_num = random.randint(10000, 99999)
        
        # Tạo dữ liệu cần thiết
        category = Category.objects.create(
            name=f'Test Cat Movement {random_num}',
            description='Test for movement'
        )
        
        unit = Unit.objects.create(
            name=f'test_unit_mv{random_num}',
            description='Test Unit for Movement'
        )
        
        product = Product.objects.create(
            code=f'TESTMV{random_num}',
            name=f'Test Product Movement {random_num}',
            category=category,
            unit=unit,
            cost_price=1500,
            selling_price=2500,
            shelf_life_days=7,
            storage_temperature_min=10,
            storage_temperature_max=20,
            humidity_requirement=75,
            hs_code='123456'
        )
        
        warehouse = Warehouse.objects.create(
            name=f'Kho Movement Test {random_num}',
            code=f'KHOMV{random_num}',
            address='Địa chỉ kho movement test',
            capacity=3000.00,
            manager=user,
            is_active=True
        )
        
        # Tạo biến động nhập kho
        movement = StockMovement.objects.create(
            warehouse=warehouse,
            product=product,
            movement_type='inbound',
            quantity=50,
            unit_cost=1500,
            notes='Test nhập kho',
            created_by=user
        )
        
        # Kiểm tra tồn kho
        try:
            stock = InventoryStock.objects.get(
                warehouse=warehouse,
                product=product
            )
            stock_quantity = stock.quantity
        except InventoryStock.DoesNotExist:
            stock_quantity = 0
        
        print(f"  ✅ Biến động kho tạo thành công:")
        print(f"    - Loại: {movement.get_movement_type_display()}")
        print(f"    - Sản phẩm: {product.name}")
        print(f"    - Số lượng: {movement.quantity}")
        print(f"    - Tồn kho sau biến động: {stock_quantity}")
        results.append(("Tạo biến động kho", True))
        
        # Cleanup
        if 'stock' in locals():
            stock.delete()
        movement.delete()
        warehouse.delete()
        product.delete()
        category.delete()
        unit.delete()
        
    except Exception as e:
        print(f"  ❌ Tạo biến động kho thất bại: {str(e)}")
        results.append(("Tạo biến động kho", False))
    
    # Test 4: Thêm sửa xóa tin tức
    print("\n📰 Test 4: Quản lý tin tức...")
    try:
        from news.models import NewsCategory
        
        # Tạo category trước
        category = NewsCategory.objects.create(
            name='Test Category News',
            description='Test category for news'
        )
        
        # Thêm tin tức
        news = News.objects.create(
            title='Tin tức test 2025',
            slug='tin-tuc-test-2025',
            summary='Tóm tắt tin tức test cho năm 2025',
            content='Nội dung tin tức test cho năm 2025',
            category=category,
            news_type='internal',
            author=user,
            status='published'
        )
        
        print(f"  ✅ Thêm tin tức: {news.title}")
        
        # Sửa tin tức
        news.title = 'Tin tức test 2025 - Đã cập nhật'
        news.content = 'Nội dung tin tức đã được cập nhật'
        news.save()
        
        print(f"  ✅ Sửa tin tức: {news.title}")
        
        # Xóa tin tức
        news_title = news.title
        news.delete()
        category.delete()
        
        print(f"  ✅ Xóa tin tức: {news_title}")
        results.append(("Quản lý tin tức", True))
        
    except Exception as e:
        print(f"  ❌ Quản lý tin tức thất bại: {str(e)}")
        results.append(("Quản lý tin tức", False))
    
    # Test 5: Tạo khách hàng mới
    print("\n🏢 Test 5: Tạo khách hàng mới...")
    try:
        import random
        random_num = random.randint(10000, 99999)
        
        customer = Company.objects.create(
            name=f'Khách hàng test {random_num}',
            company_type='limited',
            tax_code=f'KH{random_num}',
            phone=f'0901{random_num}',
            email=f'customer{random_num}@test.com',
            address=f'Địa chỉ khách hàng {random_num}',
            website=f'https://customer{random_num}.com',
            is_active=True
        )
        
        print(f"  ✅ Khách hàng tạo thành công: {customer.name}")
        print(f"    - Mã số thuế: {customer.tax_code}")
        print(f"    - Điện thoại: {customer.phone}")
        print(f"    - Email: {customer.email}")
        results.append(("Tạo khách hàng", True))
        
        customer.delete()
        
    except Exception as e:
        print(f"  ❌ Tạo khách hàng thất bại: {str(e)}")
        results.append(("Tạo khách hàng", False))
    
    # Test 6: Test URL payments
    print("\n💳 Test 6: Test trang payments...")
    try:
        # Kiểm tra nếu có payments app
        try:
            from django.urls import reverse
            payments_url = reverse('payments:list')  # Fixed: 'list' not 'payment_list'
            print(f"  ✅ Payments URL tồn tại: /payments/")
            results.append(("Payments URL", True))
        except:
            print(f"  ⚠️  Payments app chưa có hoặc URL chưa được định nghĩa")
            results.append(("Payments URL", False))
        
    except Exception as e:
        print(f"  ❌ Test payments thất bại: {str(e)}")
        results.append(("Payments URL", False))
    
    # Cleanup test user
    user.delete()
    
    # Final Summary
    print("\n" + "=" * 80)
    print("🏆 KẾT QUẢ TEST CHỨC NĂNG")
    print("=" * 80)
    
    passed = 0
    total = len(results)
    
    for test_name, result in results:
        status = "✅ THÀNH CÔNG" if result else "❌ THẤT BẠI"
        print(f"{test_name:<25} {status}")
        if result:
            passed += 1
    
    success_rate = (passed / total) * 100
    print(f"\n📊 TỶ LỆ THÀNH CÔNG: {passed}/{total} ({success_rate:.1f}%)")
    
    if success_rate == 100:
        print("🎉 HOÀN HẢO! Tất cả chức năng hoạt động tốt!")
    elif success_rate >= 80:
        print("✅ TỐT! Phần lớn chức năng hoạt động ổn định.")
    elif success_rate >= 60:
        print("⚠️  KHẤP KHIỂNG! Một số chức năng cần được kiểm tra.")
    else:
        print("❌ CẦN CẢI THIỆN! Nhiều chức năng có vấn đề.")
    
    print("\n🔧 URLs CẦN KIỂM TRA THỦ CÔNG:")
    print("📋 Tạo đơn hàng: http://127.0.0.1:8000/orders/create/")
    print("🏪 Thêm kho mới: http://127.0.0.1:8000/inventory/warehouses/create/")
    print("📦 Tạo biến động: http://127.0.0.1:8000/inventory/movements/create/")
    print("📰 Quản lý tin tức: http://127.0.0.1:8000/news/")
    print("🏢 Tạo khách hàng: http://127.0.0.1:8000/companies/create/")
    print("💳 Trang payments: http://127.0.0.1:8000/payments/")

if __name__ == '__main__':
    test_functionality()
