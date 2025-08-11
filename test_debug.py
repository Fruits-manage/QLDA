"""
Debug test for specific issues
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

def debug_issues():
    """Debug specific issues"""
    print("🔧 DEBUGGING SPECIFIC ISSUES")
    print("=" * 60)
    
    User = get_user_model()
    
    # Setup user
    user, created = User.objects.get_or_create(
        username='debuguser',
        defaults={
            'email': 'debug@example.com',
            'first_name': 'Debug',
            'last_name': 'User',
            'is_staff': True
        }
    )
    if created:
        user.set_password('testpass123')
        user.save()
    
    # Test 1: Categories field name
    print("\n🔍 Test 1: Category product count...")
    try:
        from django.db import models
        from products.models import Category
        
        # Check the correct related name
        categories = Category.objects.annotate(
            product_count=models.Count('products')  # Should be 'products' 
        ).all()
        print(f"  ✅ Category count query works: {categories.count()} categories")
        
        for cat in categories[:3]:
            print(f"    - {cat.name}: {cat.product_count} products")
            
    except Exception as e:
        print(f"  ❌ Category count failed: {str(e)}")
    
    # Test 2: Warehouse creation
    print("\n🔍 Test 2: Warehouse creation...")
    try:
        warehouse = Warehouse.objects.create(
            name='Debug Test Warehouse',
            code='DEBUG001',
            address='123 Debug Street',
            capacity=1000.00,
            manager=user,
            is_active=True
        )
        print(f"  ✅ Warehouse created: {warehouse.name}")
        warehouse.delete()
        
    except Exception as e:
        print(f"  ❌ Warehouse creation failed: {str(e)}")
    
    # Test 3: Movement creation
    print("\n🔍 Test 3: Movement creation...")
    try:
        # Create test data
        category = Category.objects.create(
            name='Debug Category',
            description='Debug category'
        )
        
        unit = Unit.objects.create(
            name='debug_kg',
            description='Debug Kilogram'
        )
        
        product = Product.objects.create(
            code='DEBUG001',
            name='Debug Product',
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
            name='Debug Warehouse',
            code='DEBUG002',
            address='123 Debug Address',
            capacity=1000.00,
            manager=user,
            is_active=True
        )
        
        movement = StockMovement.objects.create(
            warehouse=warehouse,
            product=product,
            movement_type='in',
            quantity=50,
            unit_cost=1000,
            notes='Debug movement',
            created_by=user
        )
        print(f"  ✅ Movement created: {movement.notes}")
        
        # Cleanup
        movement.delete()
        warehouse.delete()
        product.delete()
        category.delete()
        unit.delete()
        
    except Exception as e:
        print(f"  ❌ Movement creation failed: {str(e)}")
    
    # Test 4: Order creation with details
    print("\n🔍 Test 4: Order creation...")
    try:
        # Create test data
        company = Company.objects.create(
            name='Debug Order Company',
            company_type='limited',
            tax_code='DEBUG123456',
            is_active=True
        )
        
        category = Category.objects.create(
            name='Debug Order Category',
            description='Debug category'
        )
        
        unit = Unit.objects.create(
            name='debug_pcs',
            description='Debug Pieces'
        )
        
        product = Product.objects.create(
            code='DEBUGORD001',
            name='Debug Order Product',
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
        
        order = Order.objects.create(
            order_type='domestic_sale',
            company=company,
            delivery_date=date(2025, 8, 15),
            shipping_address='Debug Address',
            payment_status='pending',
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
        
        # Update order totals
        order.subtotal = 7500
        order.total_amount = 7500
        order.save()
        
        print(f"  ✅ Order created: {order.order_number}")
        print(f"    - Details: {order_detail.quantity} x {order_detail.product.name}")
        print(f"    - Total: {order.total_amount}")
        
        # Cleanup
        order_detail.delete()
        order.delete()
        company.delete()
        product.delete()
        category.delete()
        unit.delete()
        
    except Exception as e:
        print(f"  ❌ Order creation failed: {str(e)}")
    
    # Cleanup
    user.delete()
    
    print("\n" + "=" * 60)
    print("🎯 DEBUG SUMMARY")
    print("=" * 60)
    print("✅ Category field: Use 'products' not 'product'")
    print("✅ Warehouse: Should work with proper manager")
    print("✅ Movement: Requires all related objects")
    print("✅ Order: Needs proper field names in model")
    
    print("\n💡 NEXT STEPS:")
    print("🔧 Check templates for any missing variables")
    print("🔧 Verify all forms have correct field names")
    print("🔧 Test with proper user permissions")
    print("🔧 Check for any JavaScript errors in forms")

if __name__ == '__main__':
    debug_issues()
