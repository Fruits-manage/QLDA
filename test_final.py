"""
Final test để kiểm tra tất cả fixes
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
from inventory.models import Warehouse, InventoryStock, StockMovement
from accounts.models import User
from django.contrib.auth import get_user_model

def final_test():
    """Final comprehensive test"""
    print("🎯 FINAL COMPREHENSIVE TEST")
    print("=" * 80)
    
    User = get_user_model()
    
    # Setup user
    user, created = User.objects.get_or_create(
        username='finaluser',
        defaults={
            'email': 'final@example.com',
            'first_name': 'Final',
            'last_name': 'User',
            'is_staff': True
        }
    )
    if created:
        user.set_password('testpass123')
        user.save()
    
    results = []
    
    # Test 1: Product Categories (Fixed)
    print("\n✅ Test 1: Product Categories...")
    try:
        from django.db import models
        categories = Category.objects.annotate(
            product_count=models.Count('products')  # Fixed: products not product
        ).all()
        print(f"  ✅ Categories with product counts: {categories.count()}")
        results.append(("Categories", True))
    except Exception as e:
        print(f"  ❌ Categories failed: {str(e)}")
        results.append(("Categories", False))
    
    # Test 2: Order Data Saving (Fixed)
    print("\n✅ Test 2: Order Data Saving...")
    try:
        company = Company.objects.create(
            name='Final Test Company',
            company_type='limited',
            tax_code='FINAL123456',
            is_active=True
        )
        
        category = Category.objects.create(
            name='Final Test Category',
            description='Final test'
        )
        
        unit = Unit.objects.create(
            name='final_kg',
            description='Final Kilogram'
        )
        
        product = Product.objects.create(
            code='FINAL001',
            name='Final Test Product',
            category=category,
            unit=unit,
            cost_price=1000,
            selling_price=1500,
            shelf_life_days=7,
            storage_temperature_min=10,
            storage_temperature_max=15,
            humidity_requirement=85,
            hs_code='123456'
        )
        
        # Create order with correct fields
        order = Order.objects.create(
            order_type='domestic_sale',  # Fixed field
            company=company,
            delivery_date=date(2025, 8, 15),
            shipping_address='Final Test Address',
            payment_status='pending',  # Fixed field
            created_by=user
        )
        
        # Create order detail
        order_detail = OrderDetail.objects.create(
            order=order,
            product=product,
            quantity=5,
            unit_price=1500,
            total_price=7500
        )
        
        # Update totals with correct field names
        order.subtotal = 7500
        order.discount_amount = 0  # Fixed field name
        order.total_amount = 7500
        order.save()
        
        print(f"  ✅ Order saved: {order.order_number}, Total: {order.total_amount}")
        results.append(("Order Saving", True))
        
        # Cleanup
        order_detail.delete()
        order.delete()
        company.delete()
        product.delete()
        category.delete()
        unit.delete()
        
    except Exception as e:
        print(f"  ❌ Order saving failed: {str(e)}")
        results.append(("Order Saving", False))
    
    # Test 3: Inventory Movement (Fixed)
    print("\n✅ Test 3: Inventory Movement...")
    try:
        # Use unique names for each test run
        import random
        random_num = random.randint(1000, 9999)
        
        category = Category.objects.create(
            name=f'FinalMovCat{random_num}',
            description='Final movement test'
        )
        
        unit = Unit.objects.create(
            name=f'finpcs{random_num}',
            description='Final Pieces'
        )
        
        product = Product.objects.create(
            code=f'FMOV{random_num}',
            name=f'Final Movement Product {random_num}',
            category=category,
            unit=unit,
            cost_price=1000,
            selling_price=1500,
            shelf_life_days=7,
            storage_temperature_min=10,
            storage_temperature_max=15,
            humidity_requirement=85,
            hs_code='123456'
        )
        
        warehouse = Warehouse.objects.create(
            name=f'Final Test WH {random_num}',
            code=f'FWH{random_num}',
            address='Final Test Address',
            capacity=1000.00,
            manager=user,
            is_active=True
        )
        
        # Create movement
        movement = StockMovement.objects.create(
            warehouse=warehouse,
            product=product,
            movement_type='inbound',  # Changed from 'in' to 'inbound'
            quantity=100,
            unit_cost=1000,
            notes='Final test movement',
            created_by=user
        )
        
        # Check if stock was created/updated
        stock = InventoryStock.objects.get(
            warehouse=warehouse,
            product=product
        )
        
        print(f"  ✅ Movement created: {movement.notes}")
        print(f"    Stock quantity: {stock.quantity}")
        results.append(("Movement Create", True))
        
        # Cleanup
        movement.delete()
        stock.delete()
        warehouse.delete()
        product.delete()
        category.delete()
        unit.delete()
        
    except Exception as e:
        print(f"  ❌ Movement creation failed: {str(e)}")
        results.append(("Movement Create", False))
    
    # Test 4: Warehouse Creation (Fixed)
    print("\n✅ Test 4: Warehouse Creation...")
    try:
        import random
        random_num = random.randint(1000, 9999)
        
        warehouse = Warehouse.objects.create(
            name=f'Final WH Test {random_num}',
            code=f'FWH2{random_num}',
            address='Final Warehouse Address',
            capacity=2000.00,
            manager=user,
            is_active=True
        )
        
        print(f"  ✅ Warehouse created: {warehouse.name}")
        results.append(("Warehouse Create", True))
        
        warehouse.delete()
        
    except Exception as e:
        print(f"  ❌ Warehouse creation failed: {str(e)}")
        results.append(("Warehouse Create", False))
    
    # Cleanup
    user.delete()
    
    # Final Summary
    print("\n" + "=" * 80)
    print("🏆 FINAL TEST RESULTS")
    print("=" * 80)
    
    passed = 0
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"{test_name:<20} {status}")
        if result:
            passed += 1
    
    success_rate = (passed / total) * 100
    print(f"\n📊 SUCCESS RATE: {passed}/{total} ({success_rate:.1f}%)")
    
    if success_rate == 100:
        print("🎉 PERFECT! All fixes working correctly!")
    elif success_rate >= 75:
        print("✅ GOOD! Most fixes working with minor issues.")
    else:
        print("⚠️  WARNING! Some fixes still have issues.")
    
    print("\n💡 FIXED ISSUES:")
    print("✅ Categories field: 'product' → 'products'")
    print("✅ Order fields: Removed invalid fields (payment_method, discount, priority)")
    print("✅ Order saving: Fixed field names (discount_amount, payment_status)")
    print("✅ Movement saving: Added proper error handling")
    print("✅ Warehouse creation: Added error handling")
    
    print("\n🔧 URLs TO TEST MANUALLY:")
    print("http://127.0.0.1:8000/products/categories/")
    print("http://127.0.0.1:8000/orders/create/")
    print("http://127.0.0.1:8000/inventory/movements/create/")
    print("http://127.0.0.1:8000/inventory/warehouses/create/")

if __name__ == '__main__':
    final_test()
