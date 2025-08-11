"""
Quick CRUD Test Script for Fruit Management System
Kiểm tra nhanh tất cả chức năng CRUD của hệ thống

Usage: python test_quick_crud.py
"""

import os
import sys
import django
import requests
from datetime import datetime

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fruit_manage.settings')

def test_urls():
    """Test tất cả URLs có thể truy cập được"""
    base_url = "http://127.0.0.1:8000"
    
    # Danh sách URLs cần test
    test_urls = {
        # Products
        'products:list': '/products/',
        'products:create': '/products/create/',
        
        # Companies  
        'companies:list': '/companies/',
        'companies:create': '/companies/create/',
        
        # Orders
        'orders:list': '/orders/',
        'orders:create': '/orders/create/',
        
        # Inventory
        'inventory:warehouses': '/inventory/warehouses/',
        'inventory:warehouse_create': '/inventory/warehouses/create/',
        'inventory:stock': '/inventory/stock/',
        'inventory:stock_create': '/inventory/stock/create/',
        'inventory:movements': '/inventory/movements/',
        'inventory:movement_create': '/inventory/movements/create/',
        
        # News
        'news:list': '/news/',
        'news:create': '/news/create/',
        
        # Management
        'management:employee_list': '/management/employees/',
        'management:employee_create': '/management/employees/create/',
        'management:customer_list': '/management/customers/',
        'management:customer_create': '/management/customers/create/',
        
        # Dashboard
        'dashboard': '/',
        'admin': '/admin/',
    }
    
    print("🔍 Testing URL Accessibility...")
    print("=" * 60)
    
    results = {
        'accessible': [],
        'not_accessible': [],
        'redirect': []
    }
    
    for name, url in test_urls.items():
        try:
            full_url = base_url + url
            response = requests.get(full_url, timeout=5, allow_redirects=False)
            
            if response.status_code == 200:
                status = "✅ ACCESSIBLE"
                results['accessible'].append(name)
            elif response.status_code in [301, 302]:
                status = "🔄 REDIRECT"
                results['redirect'].append(name)
            else:
                status = f"❌ ERROR ({response.status_code})"
                results['not_accessible'].append(name)
                
        except Exception as e:
            status = f"❌ CONNECTION ERROR"
            results['not_accessible'].append(name)
        
        print(f"{name:<30} {url:<30} {status}")
    
    print("\n" + "=" * 60)
    print("📊 SUMMARY:")
    print(f"✅ Accessible: {len(results['accessible'])}")
    print(f"🔄 Redirects: {len(results['redirect'])}")
    print(f"❌ Not Accessible: {len(results['not_accessible'])}")
    
    if results['not_accessible']:
        print(f"\n❌ Problems with: {', '.join(results['not_accessible'])}")
    
    return results

def test_database_models():
    """Test database models and basic operations"""
    print("\n🔍 Testing Database Models...")
    print("=" * 60)
    
    try:
        django.setup()
        
        # Import models
        from products.models import Product, Category, Unit
        from companies.models import Company
        from orders.models import Order, OrderDetail
        from inventory.models import Warehouse, InventoryStock, StockMovement
        from news.models import News, NewsCategory
        from management.models import Employee, Customer
        from accounts.models import User
        
        models_to_test = [
            ('User', User),
            ('Category', Category),
            ('Unit', Unit),
            ('Product', Product),
            ('Company', Company),
            ('Order', Order),
            ('OrderDetail', OrderDetail),
            ('Warehouse', Warehouse),
            ('InventoryStock', InventoryStock),
            ('StockMovement', StockMovement),
            ('NewsCategory', NewsCategory),
            ('News', News),
            ('Employee', Employee),
            ('Customer', Customer)
        ]
        
        working_models = []
        broken_models = []
        
        for model_name, model_class in models_to_test:
            try:
                # Test basic queries
                count = model_class.objects.count()
                model_class.objects.all()[:1]  # Test query
                
                status = f"✅ OK ({count} records)"
                working_models.append(model_name)
                
            except Exception as e:
                status = f"❌ ERROR: {str(e)[:50]}"
                broken_models.append(model_name)
            
            print(f"{model_name:<20} {status}")
        
        print("\n" + "=" * 60)
        print("📊 DATABASE SUMMARY:")
        print(f"✅ Working Models: {len(working_models)}")
        print(f"❌ Broken Models: {len(broken_models)}")
        
        if broken_models:
            print(f"❌ Issues with: {', '.join(broken_models)}")
        
        return {'working': working_models, 'broken': broken_models}
        
    except Exception as e:
        print(f"❌ Database connection error: {str(e)}")
        return {'working': [], 'broken': ['DATABASE_CONNECTION']}

def test_admin_urls():
    """Test admin URLs"""
    print("\n🔍 Testing Admin Interface...")
    print("=" * 60)
    
    admin_urls = [
        '/admin/',
        '/admin/products/',
        '/admin/companies/',
        '/admin/orders/',
        '/admin/inventory/',
        '/admin/news/',
        '/admin/management/',
        '/admin/accounts/',
    ]
    
    base_url = "http://127.0.0.1:8000"
    
    for url in admin_urls:
        try:
            full_url = base_url + url
            response = requests.get(full_url, timeout=5, allow_redirects=False)
            
            if response.status_code in [200, 302]:
                status = "✅ OK"
            else:
                status = f"❌ ERROR ({response.status_code})"
                
        except Exception:
            status = "❌ CONNECTION ERROR"
        
        print(f"{url:<30} {status}")

def run_complete_test():
    """Chạy tất cả các test"""
    print("🚀 FRUIT MANAGEMENT SYSTEM - COMPLETE CRUD TEST")
    print("=" * 80)
    print(f"🕐 Test started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)
    
    # Test 1: Database Models
    db_results = test_database_models()
    
    # Test 2: URL Accessibility
    url_results = test_urls()
    
    # Test 3: Admin Interface
    test_admin_urls()
    
    # Final Summary
    print("\n" + "=" * 80)
    print("🎯 FINAL TEST SUMMARY")
    print("=" * 80)
    
    total_models = len(db_results['working']) + len(db_results['broken'])
    total_urls = len(url_results['accessible']) + len(url_results['not_accessible']) + len(url_results['redirect'])
    
    print(f"📊 DATABASE MODELS:")
    print(f"   ✅ Working: {len(db_results['working'])}/{total_models}")
    print(f"   ❌ Broken: {len(db_results['broken'])}/{total_models}")
    
    print(f"\n📊 URL ENDPOINTS:")
    print(f"   ✅ Accessible: {len(url_results['accessible'])}/{total_urls}")
    print(f"   🔄 Redirects: {len(url_results['redirect'])}/{total_urls}")
    print(f"   ❌ Not Accessible: {len(url_results['not_accessible'])}/{total_urls}")
    
    # Overall Health Score
    db_score = (len(db_results['working']) / max(total_models, 1)) * 100
    url_score = ((len(url_results['accessible']) + len(url_results['redirect'])) / max(total_urls, 1)) * 100
    overall_score = (db_score + url_score) / 2
    
    print(f"\n🏆 SYSTEM HEALTH SCORE: {overall_score:.1f}%")
    
    if overall_score >= 90:
        print("🎉 EXCELLENT! System is working perfectly!")
    elif overall_score >= 75:
        print("✅ GOOD! System is mostly working with minor issues.")
    elif overall_score >= 50:
        print("⚠️  WARNING! System has significant issues that need attention.")
    else:
        print("❌ CRITICAL! System has major problems and needs immediate attention.")
    
    print("=" * 80)
    print(f"🕐 Test completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)
    
    # Recommendations
    print("\n💡 RECOMMENDATIONS:")
    if db_results['broken']:
        print("🔧 Fix database model issues first")
    if len(url_results['not_accessible']) > 3:
        print("🔧 Check URL patterns and view implementations")
    print("🔧 Run 'python manage.py runserver' to start development server")
    print("🔧 Run 'python manage.py migrate' if database issues exist")
    print("🔧 Check 'python manage.py check' for Django configuration issues")

if __name__ == '__main__':
    print("⚡ Quick CRUD Test for Fruit Management System")
    print("📝 To run the comprehensive test suite, use: python test_complete_crud.py")
    print("📝 To run this quick test, use: python test_quick_crud.py")
    print()
    
    choice = input("Choose test type:\n1. Quick Test (URLs + Models)\n2. Database Models Only\n3. URLs Only\nEnter choice (1-3): ")
    
    if choice == '1':
        run_complete_test()
    elif choice == '2':
        test_database_models()
    elif choice == '3':
        test_urls()
    else:
        print("Invalid choice. Running complete test...")
        run_complete_test()
