"""
Simplified CRUD Test for Fruit Management System
Test CRUD operations at model level without HTTP requests
"""

import os
import sys
import django
from datetime import date, datetime

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fruit_manage.settings')
django.setup()

# Import models
from products.models import Product, Category, Unit
from companies.models import Company
from orders.models import Order, OrderDetail
from inventory.models import Warehouse, InventoryStock, StockMovement
from news.models import News, NewsCategory
from management.models import Employee, Customer
from accounts.models import User
from django.contrib.auth import get_user_model

class SimpleCRUDTest:
    """Simple CRUD test without HTTP requests"""
    
    def __init__(self):
        self.setup_test_data()
    
    def setup_test_data(self):
        """Setup test data"""
        print("🔧 Setting up test data...")
        
        # Create test user
        User = get_user_model()
        self.user, created = User.objects.get_or_create(
            username='testuser',
            defaults={
                'email': 'test@example.com',
                'first_name': 'Test',
                'last_name': 'User'
            }
        )
        if created:
            self.user.set_password('testpass123')
            self.user.save()
        
        # Create test categories and units
        self.category, _ = Category.objects.get_or_create(
            name='Trái cây tươi',
            defaults={'description': 'Các loại trái cây tươi ngon'}
        )
        
        self.unit, _ = Unit.objects.get_or_create(
            name='kg',
            defaults={'description': 'Kilogram'}
        )
        
        print("✅ Test data setup completed")
    
    def test_products_crud(self):
        """Test Products CRUD at model level"""
        print("\n🔍 Testing Products CRUD (Model Level)...")
        
        # CREATE
        try:
            product = Product.objects.create(
                code='TEST_PRD001',
                name='Test Xoài cát Hòa Lộc',
                category=self.category,
                unit=self.unit,
                description='Test product',
                origin='Test Origin',
                quality_grade='A',
                cost_price=50000,
                selling_price=80000,
                export_price=90000,
                shelf_life_days=7,
                storage_temperature_min=10,
                storage_temperature_max=15,
                humidity_requirement=85,
                hs_code='080450',
                is_active=True
            )
            print("  ✅ Product CREATE: Success")
        except Exception as e:
            print(f"  ❌ Product CREATE: Failed - {str(e)}")
            return False
        
        # READ
        try:
            retrieved_product = Product.objects.get(code='TEST_PRD001')
            assert retrieved_product.name == 'Test Xoài cát Hòa Lộc'
            
            # Test filtering
            products = Product.objects.filter(category=self.category)
            assert products.count() > 0
            print("  ✅ Product READ: Success")
        except Exception as e:
            print(f"  ❌ Product READ: Failed - {str(e)}")
            return False
        
        # UPDATE
        try:
            product.name = 'Test Xoài cát Hòa Lộc UPDATED'
            product.selling_price = 85000
            product.save()
            
            product.refresh_from_db()
            assert product.name == 'Test Xoài cát Hòa Lộc UPDATED'
            assert product.selling_price == 85000
            print("  ✅ Product UPDATE: Success")
        except Exception as e:
            print(f"  ❌ Product UPDATE: Failed - {str(e)}")
            return False
        
        # DELETE
        try:
            product_id = product.id
            product.delete()
            
            # Verify deletion
            assert not Product.objects.filter(id=product_id).exists()
            print("  ✅ Product DELETE: Success")
        except Exception as e:
            print(f"  ❌ Product DELETE: Failed - {str(e)}")
            return False
        
        print("✅ Products CRUD: ALL TESTS PASSED")
        return True
    
    def test_companies_crud(self):
        """Test Companies CRUD at model level"""
        print("\n🔍 Testing Companies CRUD (Model Level)...")
        
        # CREATE
        try:
            company = Company.objects.create(
                name='Test Công ty TNHH ABC',
                company_type='limited',
                tax_code='TEST123456789',
                address='123 Test Address',
                phone='0901234567',
                email='test@testcompany.com',
                website='https://testcompany.com',
                contact_person='Test Person',
                contact_phone='0901234567',
                contact_email='contact@testcompany.com',
                bank_name='Test Bank',
                bank_account='1234567890',
                is_active=True
            )
            print("  ✅ Company CREATE: Success")
        except Exception as e:
            print(f"  ❌ Company CREATE: Failed - {str(e)}")
            return False
        
        # READ
        try:
            retrieved_company = Company.objects.get(tax_code='TEST123456789')
            assert retrieved_company.name == 'Test Công ty TNHH ABC'
            
            # Test filtering
            companies = Company.objects.filter(company_type='limited')
            assert companies.count() > 0
            print("  ✅ Company READ: Success")
        except Exception as e:
            print(f"  ❌ Company READ: Failed - {str(e)}")
            return False
        
        # UPDATE
        try:
            company.name = 'Test Công ty TNHH ABC UPDATED'
            company.phone = '0987654321'
            company.save()
            
            company.refresh_from_db()
            assert company.name == 'Test Công ty TNHH ABC UPDATED'
            assert company.phone == '0987654321'
            print("  ✅ Company UPDATE: Success")
        except Exception as e:
            print(f"  ❌ Company UPDATE: Failed - {str(e)}")
            return False
        
        # DELETE
        try:
            company_id = company.id
            company.delete()
            
            # Verify deletion
            assert not Company.objects.filter(id=company_id).exists()
            print("  ✅ Company DELETE: Success")
        except Exception as e:
            print(f"  ❌ Company DELETE: Failed - {str(e)}")
            return False
        
        print("✅ Companies CRUD: ALL TESTS PASSED")
        return True
    
    def test_inventory_crud(self):
        """Test Inventory CRUD at model level"""
        print("\n🔍 Testing Inventory CRUD (Model Level)...")
        
        # Create dependencies first
        product = Product.objects.create(
            code='TEST_INV_PRD',
            name='Test Inventory Product',
            category=self.category,
            unit=self.unit,
            cost_price=1000,
            selling_price=1500,
            shelf_life_days=7,  # Add required field
            storage_temperature_min=10,  # Add required field
            storage_temperature_max=15,  # Add required field
            humidity_requirement=85,  # Add required field
            hs_code='123456'  # Add required field
        )
        
        # Test Warehouse CRUD
        try:
            # CREATE Warehouse
            warehouse = Warehouse.objects.create(
                name='Test Kho chính',
                code='TEST_WH001',
                address='123 Test Warehouse Address',
                capacity=1000.00,
                manager=self.user,
                is_active=True
            )
            print("  ✅ Warehouse CREATE: Success")
            
            # READ Warehouse
            retrieved_warehouse = Warehouse.objects.get(code='TEST_WH001')
            assert retrieved_warehouse.name == 'Test Kho chính'
            print("  ✅ Warehouse READ: Success")
            
            # UPDATE Warehouse
            warehouse.name = 'Test Kho chính UPDATED'
            warehouse.capacity = 1500.00
            warehouse.save()
            warehouse.refresh_from_db()
            assert warehouse.name == 'Test Kho chính UPDATED'
            print("  ✅ Warehouse UPDATE: Success")
            
        except Exception as e:
            print(f"  ❌ Warehouse CRUD: Failed - {str(e)}")
            return False
        
        # Test Stock CRUD
        try:
            # CREATE Stock
            stock = InventoryStock.objects.create(
                product=product,
                warehouse=warehouse,
                quantity=100,
                min_stock_level=10,
                max_stock_level=500
            )
            print("  ✅ Stock CREATE: Success")
            
            # READ Stock
            retrieved_stock = InventoryStock.objects.get(product=product, warehouse=warehouse)
            assert retrieved_stock.quantity == 100
            print("  ✅ Stock READ: Success")
            
            # UPDATE Stock
            stock.quantity = 150
            stock.save()
            stock.refresh_from_db()
            assert stock.quantity == 150
            print("  ✅ Stock UPDATE: Success")
            
        except Exception as e:
            print(f"  ❌ Stock CRUD: Failed - {str(e)}")
            return False
        
        # Test Movement CRUD
        try:
            # CREATE Movement
            movement = StockMovement.objects.create(
                warehouse=warehouse,
                product=product,
                movement_type='in',
                quantity=50,
                unit_cost=1000,
                notes='Test movement',
                created_by=self.user
            )
            print("  ✅ Movement CREATE: Success")
            
            # READ Movement
            movements = StockMovement.objects.filter(notes='Test movement')
            assert movements.exists()
            print("  ✅ Movement READ: Success")
            
        except Exception as e:
            print(f"  ❌ Movement CRUD: Failed - {str(e)}")
            return False
        
        # Cleanup
        try:
            warehouse.delete()
            product.delete()
            print("  ✅ Inventory DELETE: Success")
        except Exception as e:
            print(f"  ❌ Inventory DELETE: Failed - {str(e)}")
        
        print("✅ Inventory CRUD: ALL TESTS PASSED")
        return True
    
    def test_orders_crud(self):
        """Test Orders CRUD at model level"""
        print("\n🔍 Testing Orders CRUD (Model Level)...")
        
        # Create dependencies
        company = Company.objects.create(
            name='Test Order Company',
            company_type='limited',
            tax_code='ORDER123456',
            is_active=True
        )
        
        product = Product.objects.create(
            code='TEST_ORDER_PRD',
            name='Test Order Product',
            category=self.category,
            unit=self.unit,
            cost_price=1000,
            selling_price=1500,
            shelf_life_days=7,  # Add required field
            storage_temperature_min=10,  # Add required field
            storage_temperature_max=15,  # Add required field
            humidity_requirement=85,  # Add required field
            hs_code='123456'  # Add required field
        )
        
        try:
            # CREATE Order
            order = Order.objects.create(
                order_type='domestic_sale',  # Use correct field
                company=company,
                delivery_date=date(2025, 8, 15),
                shipping_address='123 Test Order Address',
                notes='Test order',
                discount_amount=0,  # Use correct field name
                payment_status='pending',  # Use correct field name
                created_by=self.user
            )
            print("  ✅ Order CREATE: Success")
            
            # CREATE OrderDetail
            order_detail = OrderDetail.objects.create(
                order=order,
                product=product,
                quantity=5,
                unit_price=1500
            )
            print("  ✅ OrderDetail CREATE: Success")
            
            # READ Order
            retrieved_order = Order.objects.get(id=order.id)
            assert retrieved_order.company == company
            
            order_details = OrderDetail.objects.filter(order=order)
            assert order_details.count() == 1
            print("  ✅ Order READ: Success")
            
            # UPDATE Order
            order.status = 'confirmed'  # Use correct field and value
            order.notes = 'Test order UPDATED'
            order.save()
            order.refresh_from_db()
            assert order.status == 'confirmed'
            print("  ✅ Order UPDATE: Success")
            
            # DELETE Order (this will cascade to OrderDetail)
            order_id = order.id
            order.delete()
            assert not Order.objects.filter(id=order_id).exists()
            print("  ✅ Order DELETE: Success")
            
        except Exception as e:
            print(f"  ❌ Orders CRUD: Failed - {str(e)}")
            return False
        finally:
            # Cleanup
            company.delete()
            product.delete()
        
        print("✅ Orders CRUD: ALL TESTS PASSED")
        return True
    
    def test_news_crud(self):
        """Test News CRUD at model level"""
        print("\n🔍 Testing News CRUD (Model Level)...")
        
        # Create news category
        news_category, _ = NewsCategory.objects.get_or_create(
            name='Test News Category',
            defaults={'description': 'Test category for news'}
        )
        
        try:
            # CREATE News
            news = News.objects.create(
                title='Test Tin tức',
                summary='Test summary',
                content='Test content details',
                category=news_category,
                news_type='internal',
                status='published',
                priority='normal',
                author=self.user
            )
            print("  ✅ News CREATE: Success")
            
            # READ News
            retrieved_news = News.objects.get(title='Test Tin tức')
            assert retrieved_news.summary == 'Test summary'
            
            news_list = News.objects.filter(category=news_category)
            assert news_list.count() > 0
            print("  ✅ News READ: Success")
            
            # UPDATE News
            news.title = 'Test Tin tức UPDATED'
            news.status = 'draft'
            news.save()
            news.refresh_from_db()
            assert news.title == 'Test Tin tức UPDATED'
            assert news.status == 'draft'
            print("  ✅ News UPDATE: Success")
            
            # DELETE News
            news_id = news.id
            news.delete()
            assert not News.objects.filter(id=news_id).exists()
            print("  ✅ News DELETE: Success")
            
        except Exception as e:
            print(f"  ❌ News CRUD: Failed - {str(e)}")
            return False
        
        print("✅ News CRUD: ALL TESTS PASSED")
        return True
    
    def test_management_crud(self):
        """Test Management CRUD at model level"""
        print("\n🔍 Testing Management CRUD (Model Level)...")
        
        try:
            # Test Employee CRUD
            # CREATE Employee
            employee = Employee.objects.create(
                employee_id='TEST_EMP001',
                first_name='Test Nguyễn',
                last_name='Test Văn',
                gender='male',
                date_of_birth=date(1990, 1, 1),
                email='testemployee@test.com',
                phone='0901234567',
                address='123 Test Employee Address',
                department='sales',
                position='Test Sales Staff',
                hire_date=date(2025, 1, 1),
                salary=10000000,
                education_level='bachelor',
                marital_status='single',
                is_active=True
            )
            print("  ✅ Employee CREATE: Success")
            
            # READ Employee
            retrieved_employee = Employee.objects.get(employee_id='TEST_EMP001')
            assert retrieved_employee.first_name == 'Test Nguyễn'
            print("  ✅ Employee READ: Success")
            
            # UPDATE Employee
            employee.salary = 12000000
            employee.position = 'Senior Sales Staff'
            employee.save()
            employee.refresh_from_db()
            assert employee.salary == 12000000
            print("  ✅ Employee UPDATE: Success")
            
            # Test Customer CRUD
            # CREATE Customer
            customer = Customer.objects.create(
                customer_code='TEST_CUS001',
                name='Test Khách hàng',
                customer_type='business',
                email='testcustomer@test.com',
                phone='0901234567',
                address='123 Test Customer Address',
                tax_code='CUST987654321',
                representative_name='Test Representative',
                priority='medium',
                is_vip=False,
                credit_limit=50000000,
                payment_terms=30,
                is_active=True
            )
            print("  ✅ Customer CREATE: Success")
            
            # READ Customer
            retrieved_customer = Customer.objects.get(customer_code='TEST_CUS001')
            assert retrieved_customer.name == 'Test Khách hàng'
            print("  ✅ Customer READ: Success")
            
            # UPDATE Customer
            customer.credit_limit = 75000000
            customer.is_vip = True
            customer.save()
            customer.refresh_from_db()
            assert customer.credit_limit == 75000000
            assert customer.is_vip == True
            print("  ✅ Customer UPDATE: Success")
            
            # DELETE Employee and Customer
            employee.delete()
            customer.delete()
            assert not Employee.objects.filter(employee_id='TEST_EMP001').exists()
            assert not Customer.objects.filter(customer_code='TEST_CUS001').exists()
            print("  ✅ Management DELETE: Success")
            
        except Exception as e:
            print(f"  ❌ Management CRUD: Failed - {str(e)}")
            return False
        
        print("✅ Management CRUD: ALL TESTS PASSED")
        return True
    
    def run_all_tests(self):
        """Run all CRUD tests"""
        print("🚀 FRUIT MANAGEMENT SYSTEM - MODEL LEVEL CRUD TESTS")
        print("=" * 80)
        print(f"🕐 Test started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 80)
        
        test_results = {
            'Products': self.test_products_crud(),
            'Companies': self.test_companies_crud(),
            'Inventory': self.test_inventory_crud(),
            'Orders': self.test_orders_crud(),
            'News': self.test_news_crud(),
            'Management': self.test_management_crud()
        }
        
        print("\n" + "=" * 80)
        print("🎯 FINAL TEST SUMMARY")
        print("=" * 80)
        
        passed = sum(1 for result in test_results.values() if result)
        total = len(test_results)
        
        for module, result in test_results.items():
            status = "✅ PASSED" if result else "❌ FAILED"
            print(f"{module:<15} {status}")
        
        print("\n" + "=" * 80)
        success_rate = (passed / total) * 100
        print(f"📊 SUCCESS RATE: {passed}/{total} ({success_rate:.1f}%)")
        
        if success_rate == 100:
            print("🎉 EXCELLENT! All CRUD operations working perfectly!")
        elif success_rate >= 80:
            print("✅ GOOD! Most CRUD operations working with minor issues.")
        elif success_rate >= 60:
            print("⚠️  WARNING! Some CRUD operations have issues.")
        else:
            print("❌ CRITICAL! Major CRUD operations are failing.")
        
        print("=" * 80)
        print(f"🕐 Test completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 80)
        
        return test_results

def main():
    """Main function"""
    print("🔬 SIMPLIFIED CRUD TEST - MODEL LEVEL ONLY")
    print("📝 This test focuses on database models without HTTP requests")
    print("📝 For full HTTP tests, fix ALLOWED_HOSTS and run test_complete_crud.py")
    print()
    
    try:
        test_suite = SimpleCRUDTest()
        results = test_suite.run_all_tests()
        
        # Return appropriate exit code
        all_passed = all(results.values())
        return 0 if all_passed else 1
        
    except Exception as e:
        print(f"❌ CRITICAL ERROR: {str(e)}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == '__main__':
    exit_code = main()
    sys.exit(exit_code)
