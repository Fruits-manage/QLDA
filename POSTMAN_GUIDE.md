# HƯỚNG DẪN SỬ DỤNG POSTMAN CHO API TẠO ĐƠN HÀNG

## 🚀 Setup Postman

### 1. Tạo đơn hàng mới
**URL:** `POST http://127.0.0.1:8000/orders/api/create/`

**Headers:**
```
Content-Type: application/json
```

**Body (JSON):**
```json
{
    "company_id": 23,
    "order_type": "domestic_sale",
    "delivery_date": "2025-08-20",
    "shipping_address": "Số 222 Trần Duy Hưng, Cầu Giấy, Hà Nội",
    "payment_status": "pending",
    "notes": "Đơn hàng test từ Postman",
    "discount_amount": 100000,
    "created_by_id": 1,
    "order_details": [
        {
            "product_id": 32,
            "quantity": 10,
            "unit_price": 120000
        },
        {
            "product_id": 33,
            "quantity": 5,
            "unit_price": 200000
        }
    ]
}
```

**Giải thích các trường:**
- `company_id`: ID của công ty/khách hàng (bắt buộc)
- `order_type`: Loại đơn hàng (`domestic_sale`, `export_sale`, `import_purchase`, `domestic_purchase`)
- `delivery_date`: Ngày giao hàng (định dạng YYYY-MM-DD)
- `shipping_address`: Địa chỉ giao hàng (optional, mặc định lấy địa chỉ công ty)
- `payment_status`: Trạng thái thanh toán (`pending`, `partially_paid`, `fully_paid`)
- `notes`: Ghi chú (optional)
- `discount_amount`: Số tiền giảm giá (optional, mặc định 0)
- `created_by_id`: ID người tạo (optional, mặc định 1)
- `order_details`: Array các sản phẩm trong đơn hàng (bắt buộc)
  - `product_id`: ID sản phẩm (bắt buộc)
  - `quantity`: Số lượng (bắt buộc)
  - `unit_price`: Đơn giá (optional, mặc định lấy giá bán của sản phẩm)

**Response thành công:**
```json
{
    "success": true,
    "order_id": 15,
    "order_number": "DO-000015",
    "total_amount": 2000000.0,
    "message": "Order created successfully"
}
```

**Response lỗi:**
```json
{
    "success": false,
    "error": "Missing required field: company_id"
}
```

### 2. Lấy thông tin đơn hàng
**URL:** `GET http://127.0.0.1:8000/orders/api/15/`

**Response:**
```json
{
    "success": true,
    "order": {
        "id": 15,
        "order_number": "DO-000015",
        "order_type": "domestic_sale",
        "company": {
            "id": 1,
            "name": "Siêu thị BigC Thăng Long",
            "tax_code": "0106123456"
        },
        "delivery_date": "2025-08-20",
        "shipping_address": "Số 222 Trần Duy Hưng, Cầu Giấy, Hà Nội",
        "payment_status": "pending",
        "status": "pending",
        "subtotal": 2100000.0,
        "discount_amount": 100000.0,
        "total_amount": 2000000.0,
        "notes": "Đơn hàng test từ Postman",
        "created_at": "2025-08-09T21:25:00.123456Z",
        "order_details": [
            {
                "id": 101,
                "product": {
                    "id": 1,
                    "code": "APPLE001",
                    "name": "Táo Fuji Nhật Bản"
                },
                "quantity": 10.0,
                "unit_price": 120000.0,
                "total_price": 1200000.0
            },
            {
                "id": 102,
                "product": {
                    "id": 2,
                    "code": "ORANGE001",
                    "name": "Cam sành Việt Nam"
                },
                "quantity": 5.0,
                "unit_price": 200000.0,
                "total_price": 1000000.0
            }
        ]
    }
}
```

## 📋 Các bước test trong Postman

### Bước 1: Lấy danh sách Company
**URL:** `GET http://127.0.0.1:8000/companies/api/` (nếu có API)
Hoặc check database để lấy company_id

### Bước 2: Lấy danh sách Product
**URL:** `GET http://127.0.0.1:8000/products/api/` (nếu có API)
Hoặc check database để lấy product_id

### Bước 3: Tạo đơn hàng
Sử dụng JSON template ở trên với company_id và product_id thực tế

### Bước 4: Kiểm tra đơn hàng
Sử dụng order_id từ response để GET thông tin chi tiết

## 🔧 Troubleshooting

### Lỗi 400 - Bad Request
- Kiểm tra JSON format
- Đảm bảo có đủ required fields
- Kiểm tra company_id và product_id có tồn tại

### Lỗi 404 - Not Found
- Kiểm tra URL có đúng không
- Đảm bảo server đang chạy

### Lỗi 500 - Internal Server Error
- Kiểm tra server logs
- Đảm bảo database connection ổn

## 📊 Dữ liệu test có sẵn

Từ script `create_test_orders.py` đã tạo:

**Companies:**
- ID: 1 - "Siêu thị BigC Thăng Long" (tax_code: 0106123456)
- ID: 2 - "Cửa hàng trái cây Sạch" (tax_code: 0106789012)

**Products:**
- ID: 1 - "Táo Fuji Nhật Bản" (code: APPLE001, price: 120000)
- ID: 2 - "Cam sành Việt Nam" (code: ORANGE001, price: 200000)  
- ID: 3 - "Nho xanh Úc" (code: GRAPE001, price: 280000)

**Test User:**
- Username: ordertest2025
- Password: test123456
