"""
Test API tạo đơn hàng
"""

import requests
import json

# Base URL
BASE_URL = "http://127.0.0.1:8000"

def test_create_order():
    """Test tạo đơn hàng qua API"""
    
    # Data để tạo đơn hàng
    order_data = {
        "company_id": 23,  # Siêu thị BigC Thăng Long
        "order_type": "domestic_sale",
        "delivery_date": "2025-08-25",
        "shipping_address": "Số 222 Trần Duy Hưng, Cầu Giấy, Hà Nội",
        "payment_status": "pending",
        "notes": "Đơn hàng test từ Python API",
        "discount_amount": 50000,
        "created_by_id": 1,
        "order_details": [
            {
                "product_id": 32,  # Táo Fuji
                "quantity": 20,
                "unit_price": 120000
            },
            {
                "product_id": 33,  # Cam sành
                "quantity": 10,
                "unit_price": 200000
            },
            {
                "product_id": 34,  # Nho xanh
                "quantity": 5,
                "unit_price": 280000
            }
        ]
    }
    
    print("🚀 TESTING ORDER API")
    print("=" * 50)
    
    # Test tạo đơn hàng
    print("\n📋 Test 1: Tạo đơn hàng...")
    try:
        response = requests.post(
            f"{BASE_URL}/orders/api/create/",
            json=order_data,
            headers={"Content-Type": "application/json"}
        )
        
        print(f"Status Code: {response.status_code}")
        result = response.json()
        print(f"Response: {json.dumps(result, indent=2, ensure_ascii=False)}")
        
        if result.get('success'):
            order_id = result['order_id']
            print(f"\n✅ Đơn hàng tạo thành công! ID: {order_id}")
            
            # Test lấy thông tin đơn hàng
            print(f"\n📄 Test 2: Lấy thông tin đơn hàng {order_id}...")
            detail_response = requests.get(f"{BASE_URL}/orders/api/{order_id}/")
            print(f"Status Code: {detail_response.status_code}")
            detail_result = detail_response.json()
            print(f"Response: {json.dumps(detail_result, indent=2, ensure_ascii=False)}")
            
            if detail_result.get('success'):
                order = detail_result['order']
                print(f"\n✅ Thông tin đơn hàng:")
                print(f"  - Mã đơn: {order['order_number']}")
                print(f"  - Khách hàng: {order['company']['name']}")
                print(f"  - Tổng tiền: {order['total_amount']:,} VND")
                print(f"  - Số sản phẩm: {len(order['order_details'])}")
            else:
                print(f"❌ Lỗi lấy thông tin: {detail_result.get('error')}")
        else:
            print(f"❌ Lỗi tạo đơn hàng: {result.get('error')}")
            
    except requests.exceptions.ConnectionError:
        print("❌ Không thể kết nối đến server. Đảm bảo server đang chạy!")
    except Exception as e:
        print(f"❌ Lỗi: {str(e)}")

def test_invalid_data():
    """Test với dữ liệu không hợp lệ"""
    print("\n🧪 Test 3: Test dữ liệu không hợp lệ...")
    
    # Missing required field
    invalid_data = {
        "order_type": "domestic_sale",
        "delivery_date": "2025-08-25"
        # Missing company_id and order_details
    }
    
    try:
        response = requests.post(
            f"{BASE_URL}/orders/api/create/",
            json=invalid_data,
            headers={"Content-Type": "application/json"}
        )
        
        print(f"Status Code: {response.status_code}")
        result = response.json()
        print(f"Response: {json.dumps(result, indent=2, ensure_ascii=False)}")
        
        if not result.get('success'):
            print(f"✅ Validation working: {result.get('error')}")
        
    except Exception as e:
        print(f"❌ Lỗi: {str(e)}")

def print_postman_guide():
    """In hướng dẫn Postman"""
    print("\n" + "=" * 60)
    print("📚 HƯỚNG DẪN SỬ DỤNG POSTMAN")
    print("=" * 60)
    
    print("\n🔗 URL: POST http://127.0.0.1:8000/orders/api/create/")
    print("\n📋 Headers:")
    print("Content-Type: application/json")
    
    print("\n📄 Body (JSON):")
    sample_json = {
        "company_id": 23,
        "order_type": "domestic_sale",
        "delivery_date": "2025-08-25",
        "shipping_address": "Địa chỉ giao hàng",
        "payment_status": "pending",
        "notes": "Ghi chú đơn hàng",
        "discount_amount": 50000,
        "order_details": [
            {
                "product_id": 32,
                "quantity": 10,
                "unit_price": 120000
            }
        ]
    }
    print(json.dumps(sample_json, indent=2, ensure_ascii=False))
    
    print("\n💡 Các order_type có thể sử dụng:")
    print("- domestic_sale: Bán hàng nội địa")
    print("- export_sale: Xuất khẩu")
    print("- import_purchase: Nhập khẩu")
    print("- domestic_purchase: Mua hàng nội địa")
    
    print("\n💡 Các payment_status có thể sử dụng:")
    print("- pending: Chờ thanh toán")
    print("- partially_paid: Thanh toán một phần")
    print("- fully_paid: Đã thanh toán đủ")

if __name__ == '__main__':
    test_create_order()
    test_invalid_data()
    print_postman_guide()
