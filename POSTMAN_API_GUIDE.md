# Hướng dẫn sử dụng Postman với Django API

## Mục lục
1. [Thiết lập cơ bản](#thiết-lập-cơ-bản)
2. [API Đơn hàng (Orders)](#api-đơn-hàng-orders)
3. [API Công ty/Khách hàng (Companies)](#api-công-ty-khách-hàng-companies)
4. [API Kho hàng (Warehouses)](#api-kho-hàng-warehouses)
5. [API Tin tức (News)](#api-tin-tức-news)
6. [Xử lý lỗi và troubleshooting](#xử-lý-lỗi-và-troubleshooting)

## Thiết lập cơ bản

### 1. URL gốc của API
```
Base URL: http://127.0.0.1:8000
```

### 2. Headers cần thiết
Đối với tất cả các request POST/PUT/PATCH:
```
Content-Type: application/json
Accept: application/json
```

### 3. Xác thực (Authentication)
Hệ thống sử dụng Django session authentication. Đối với API testing, các endpoint được thiết kế để bypass authentication để dễ dàng test.

---

## API Đơn hàng (Orders)

### 1. Tạo đơn hàng mới

**Endpoint:** `POST /orders/api/create/`

**Request Body:**
```json
{
    "order_type": "export_sale",
    "company_id": 1,
    "delivery_date": "2024-12-31",
    "shipping_address": "123 Đường ABC, Quận 1, TP.HCM",
    "notes": "Ghi chú đặc biệt cho đơn hàng",
    "payment_status": "pending",
    "priority": "high",
    "discount_percent": 5.0,
    "products": [
        {
            "product_id": 1,
            "quantity": 10,
            "unit_price": 150000
        },
        {
            "product_id": 2,
            "quantity": 5,
            "unit_price": 200000
        }
    ]
}
```

**Response thành công (200):**
```json
{
    "success": true,
    "message": "Tạo đơn hàng thành công",
    "data": {
        "id": 123,
        "order_number": "ORD20241201001",
        "order_type": "export_sale",
        "company_id": 1,
        "company_name": "Công ty ABC",
        "subtotal": 2500000.00,
        "discount_amount": 125000.00,
        "total_amount": 2375000.00,
        "delivery_date": "2024-12-31",
        "status": "draft",
        "payment_status": "pending",
        "created_at": "2024-12-01T10:30:00.000Z",
        "products": [
            {
                "product_id": 1,
                "product_name": "Sản phẩm A",
                "quantity": 10.0,
                "unit_price": 150000.0,
                "total_price": 1500000.0
            }
        ]
    }
}
```

### 2. Xem chi tiết đơn hàng

**Endpoint:** `GET /orders/api/{order_id}/`

**Ví dụ:** `GET /orders/api/123/`

**Response thành công (200):**
```json
{
    "success": true,
    "data": {
        "id": 123,
        "order_number": "ORD20241201001",
        "order_type": "export_sale",
        "order_type_display": "Xuất khẩu",
        "company": {
            "id": 1,
            "name": "Công ty ABC",
            "contact_person": "Nguyễn Văn A",
            "phone": "0123456789"
        },
        "subtotal": 2500000.00,
        "discount_amount": 125000.00,
        "total_amount": 2375000.00,
        "delivery_date": "2024-12-31",
        "shipping_address": "123 Đường ABC, Quận 1, TP.HCM",
        "notes": "Ghi chú đặc biệt cho đơn hàng",
        "status": "draft",
        "payment_status": "pending",
        "created_at": "2024-12-01T10:30:00.000Z",
        "products": [
            {
                "id": 1,
                "product_name": "Sản phẩm A",
                "product_code": "SP001",
                "quantity": 10.0,
                "unit_price": 150000.0,
                "total_price": 1500000.0,
                "unit": "cái"
            }
        ]
    }
}
```

---

## API Công ty/Khách hàng (Companies)

### 1. Tạo công ty/khách hàng mới

**Endpoint:** `POST /companies/api/create/`

**Request Body:**
```json
{
    "name": "Công ty TNHH ABC",
    "company_type": "customer",
    "tax_code": "0123456789",
    "address": "123 Đường Nguyễn Văn Cừ, Quận 5, TP.HCM",
    "phone": "028-12345678",
    "email": "contact@abc.com",
    "website": "https://abc.com",
    "contact_person": "Nguyễn Văn A",
    "contact_phone": "0987654321",
    "contact_email": "nguyen.a@abc.com",
    "bank_name": "Ngân hàng Vietcombank",
    "bank_account": "1234567890",
    "import_license": "NK-2024-001",
    "export_license": "XK-2024-001",
    "is_active": true
}
```

**Các giá trị hợp lệ cho `company_type`:**
- `our_company`: Công ty chúng tôi
- `supplier`: Nhà cung cấp
- `customer`: Khách hàng
- `partner`: Đối tác

**Response thành công (200):**
```json
{
    "success": true,
    "message": "Tạo công ty thành công",
    "data": {
        "id": 15,
        "name": "Công ty TNHH ABC",
        "company_type": "customer",
        "tax_code": "0123456789",
        "address": "123 Đường Nguyễn Văn Cừ, Quận 5, TP.HCM",
        "phone": "028-12345678",
        "email": "contact@abc.com",
        "website": "https://abc.com",
        "contact_person": "Nguyễn Văn A",
        "contact_phone": "0987654321",
        "contact_email": "nguyen.a@abc.com",
        "bank_name": "Ngân hàng Vietcombank",
        "bank_account": "1234567890",
        "import_license": "NK-2024-001",
        "export_license": "XK-2024-001",
        "is_active": true,
        "created_at": "2024-12-01T10:45:00.000Z",
        "updated_at": "2024-12-01T10:45:00.000Z"
    }
}
```

### 2. Xem danh sách công ty

**Endpoint:** `GET /companies/api/list/`

**Query Parameters (tùy chọn):**
- `type`: Lọc theo loại công ty (customer, supplier, partner, our_company)
- `search`: Tìm kiếm theo tên, mã số thuế, hoặc người liên hệ

**Ví dụ:** `GET /companies/api/list/?type=customer&search=ABC`

**Response thành công (200):**
```json
{
    "success": true,
    "count": 2,
    "data": [
        {
            "id": 15,
            "name": "Công ty TNHH ABC",
            "company_type": "customer",
            "company_type_display": "Khách hàng",
            "tax_code": "0123456789",
            "address": "123 Đường Nguyễn Văn Cừ, Quận 5, TP.HCM",
            "phone": "028-12345678",
            "email": "contact@abc.com",
            "contact_person": "Nguyễn Văn A",
            "contact_phone": "0987654321",
            "is_active": true
        }
    ]
}
```

### 3. Xem chi tiết công ty

**Endpoint:** `GET /companies/api/{company_id}/`

**Ví dụ:** `GET /companies/api/15/`

**Response thành công (200):**
```json
{
    "success": true,
    "data": {
        "id": 15,
        "name": "Công ty TNHH ABC",
        "company_type": "customer",
        "company_type_display": "Khách hàng",
        "tax_code": "0123456789",
        "address": "123 Đường Nguyễn Văn Cừ, Quận 5, TP.HCM",
        "phone": "028-12345678",
        "email": "contact@abc.com",
        "website": "https://abc.com",
        "contact_person": "Nguyễn Văn A",
        "contact_phone": "0987654321",
        "contact_email": "nguyen.a@abc.com",
        "bank_name": "Ngân hàng Vietcombank",
        "bank_account": "1234567890",
        "import_license": "NK-2024-001",
        "export_license": "XK-2024-001",
        "is_active": true,
        "created_at": "2024-12-01T10:45:00.000Z",
        "updated_at": "2024-12-01T10:45:00.000Z"
    }
}
```

---

## API Kho hàng (Warehouses)

### 1. Tạo kho hàng mới

**Endpoint:** `POST /inventory/api/warehouses/create/`

**Request Body:**
```json
{
    "name": "Kho Tổng Quận 1",
    "code": "WH001",
    "address": "456 Đường Pasteur, Quận 1, TP.HCM",
    "manager_id": 2,
    "capacity": 1000.50,
    "is_active": true
}
```

**Lưu ý:**
- `manager_id` là ID của người dùng trong hệ thống (có thể bỏ trống)
- `capacity` tính bằng tấn

**Response thành công (200):**
```json
{
    "success": true,
    "message": "Tạo kho thành công",
    "data": {
        "id": 8,
        "name": "Kho Tổng Quận 1",
        "code": "WH001",
        "address": "456 Đường Pasteur, Quận 1, TP.HCM",
        "manager_id": 2,
        "manager_name": "Trần Thị B",
        "capacity": 1000.5,
        "is_active": true,
        "created_at": "2024-12-01T11:00:00.000Z"
    }
}
```

### 2. Xem danh sách kho hàng

**Endpoint:** `GET /inventory/api/warehouses/list/`

**Query Parameters (tùy chọn):**
- `search`: Tìm kiếm theo tên, mã kho, hoặc địa chỉ

**Ví dụ:** `GET /inventory/api/warehouses/list/?search=Quận 1`

**Response thành công (200):**
```json
{
    "success": true,
    "count": 1,
    "data": [
        {
            "id": 8,
            "name": "Kho Tổng Quận 1",
            "code": "WH001",
            "address": "456 Đường Pasteur, Quận 1, TP.HCM",
            "manager_name": "Trần Thị B",
            "capacity": 1000.5,
            "is_active": true,
            "stock_summary": {
                "total_products": 25,
                "total_quantity": 1500.0
            }
        }
    ]
}
```

### 3. Xem chi tiết kho hàng

**Endpoint:** `GET /inventory/api/warehouses/{warehouse_id}/`

**Ví dụ:** `GET /inventory/api/warehouses/8/`

**Response thành công (200):**
```json
{
    "success": true,
    "data": {
        "id": 8,
        "name": "Kho Tổng Quận 1",
        "code": "WH001",
        "address": "456 Đường Pasteur, Quận 1, TP.HCM",
        "manager_id": 2,
        "manager_name": "Trần Thị B",
        "manager_email": "tran.b@company.com",
        "capacity": 1000.5,
        "is_active": true,
        "created_at": "2024-12-01T11:00:00.000Z",
        "stock_summary": {
            "total_products": 25,
            "total_quantity": 1500.0,
            "low_stock_items": 3
        }
    }
}
```

---

## API Tin tức (News)

### 1. Tạo tin tức mới

**Endpoint:** `POST /news/api/create/`

**Request Body:**
```json
{
    "title": "Thông báo chính sách mới về xuất nhập khẩu",
    "summary": "Bộ Công Thương vừa ban hành quy định mới về thủ tục xuất nhập khẩu có hiệu lực từ ngày 1/1/2025",
    "content": "<p>Nội dung chi tiết về chính sách mới...</p><p>Các doanh nghiệp cần lưu ý những điểm sau:</p><ul><li>Điểm 1</li><li>Điểm 2</li></ul>",
    "category_id": 1,
    "news_type": "regulation",
    "status": "published",
    "priority": "high",
    "expiry_date": "2025-12-31",
    "is_featured": true,
    "is_active": true
}
```

**Các giá trị hợp lệ:**

**`news_type`:**
- `internal`: Tin nội bộ
- `industry`: Tin ngành
- `system`: Thông báo hệ thống
- `regulation`: Quy định mới
- `market`: Thị trường

**`status`:**
- `draft`: Nháp
- `published`: Đã xuất bản
- `archived`: Lưu trữ

**`priority`:**
- `low`: Thấp
- `normal`: Bình thường
- `high`: Cao
- `urgent`: Khẩn cấp

**Response thành công (200):**
```json
{
    "success": true,
    "message": "Tạo tin tức thành công",
    "data": {
        "id": 45,
        "title": "Thông báo chính sách mới về xuất nhập khẩu",
        "slug": "thong-bao-chinh-sach-moi-ve-xuat-nhap-khau",
        "summary": "Bộ Công Thương vừa ban hành quy định mới về thủ tục xuất nhập khẩu có hiệu lực từ ngày 1/1/2025",
        "content": "<p>Nội dung chi tiết về chính sách mới...</p>",
        "category_id": 1,
        "category_name": "Quy định pháp luật",
        "news_type": "regulation",
        "status": "published",
        "priority": "high",
        "author_id": 1,
        "author_name": "Admin User",
        "publish_date": "2024-12-01T11:15:00.000Z",
        "expiry_date": "2025-12-31T00:00:00.000Z",
        "is_featured": true,
        "is_active": true,
        "views_count": 0,
        "created_at": "2024-12-01T11:15:00.000Z",
        "updated_at": "2024-12-01T11:15:00.000Z"
    }
}
```

### 2. Xem danh sách tin tức

**Endpoint:** `GET /news/api/list/`

**Query Parameters (tùy chọn):**
- `status`: Lọc theo trạng thái (draft, published, archived)
- `category_id`: Lọc theo danh mục
- `news_type`: Lọc theo loại tin
- `search`: Tìm kiếm trong tiêu đề, tóm tắt, nội dung
- `is_featured`: Lọc tin nổi bật (true/false)
- `order_by`: Sắp xếp theo (created_at, -created_at, title, -title, views_count, -views_count)

**Ví dụ:** `GET /news/api/list/?status=published&news_type=regulation&is_featured=true&order_by=-created_at`

**Response thành công (200):**
```json
{
    "success": true,
    "count": 1,
    "data": [
        {
            "id": 45,
            "title": "Thông báo chính sách mới về xuất nhập khẩu",
            "slug": "thong-bao-chinh-sach-moi-ve-xuat-nhap-khau",
            "summary": "Bộ Công Thương vừa ban hành quy định mới...",
            "category": {
                "id": 1,
                "name": "Quy định pháp luật",
                "color": "#dc3545"
            },
            "news_type": "regulation",
            "news_type_display": "Quy định mới",
            "status": "published",
            "status_display": "Đã xuất bản",
            "priority": "high",
            "priority_display": "Cao",
            "author_name": "Admin User",
            "publish_date": "2024-12-01T11:15:00.000Z",
            "is_featured": true,
            "views_count": 15,
            "created_at": "2024-12-01T11:15:00.000Z"
        }
    ]
}
```

### 3. Xem chi tiết tin tức

**Endpoint:** `GET /news/api/{news_id}/`

**Ví dụ:** `GET /news/api/45/`

**Lưu ý:** API này sẽ tự động tăng số lượt xem của tin tức.

**Response thành công (200):**
```json
{
    "success": true,
    "data": {
        "id": 45,
        "title": "Thông báo chính sách mới về xuất nhập khẩu",
        "slug": "thong-bao-chinh-sach-moi-ve-xuat-nhap-khau",
        "summary": "Bộ Công Thương vừa ban hành quy định mới về thủ tục xuất nhập khẩu có hiệu lực từ ngày 1/1/2025",
        "content": "<p>Nội dung chi tiết về chính sách mới...</p><p>Các doanh nghiệp cần lưu ý những điểm sau:</p><ul><li>Điểm 1</li><li>Điểm 2</li></ul>",
        "category": {
            "id": 1,
            "name": "Quy định pháp luật",
            "color": "#dc3545"
        },
        "news_type": "regulation",
        "news_type_display": "Quy định mới",
        "status": "published",
        "status_display": "Đã xuất bản",
        "priority": "high",
        "priority_display": "Cao",
        "author": {
            "id": 1,
            "name": "Admin User",
            "email": "admin@company.com"
        },
        "publish_date": "2024-12-01T11:15:00.000Z",
        "expiry_date": "2025-12-31T00:00:00.000Z",
        "is_featured": true,
        "is_active": true,
        "views_count": 16,
        "created_at": "2024-12-01T11:15:00.000Z",
        "updated_at": "2024-12-01T11:15:00.000Z"
    }
}
```

### 4. Xem danh sách danh mục tin tức

**Endpoint:** `GET /news/api/categories/`

**Response thành công (200):**
```json
{
    "success": true,
    "count": 3,
    "data": [
        {
            "id": 1,
            "name": "Quy định pháp luật",
            "description": "Các quy định mới từ cơ quan chức năng",
            "color": "#dc3545",
            "is_active": true,
            "news_count": 12
        },
        {
            "id": 2,
            "name": "Thị trường",
            "description": "Thông tin về thị trường xuất nhập khẩu",
            "color": "#28a745",
            "is_active": true,
            "news_count": 8
        }
    ]
}
```

---

## Xử lý lỗi và Troubleshooting

### Các mã lỗi phổ biến

**400 Bad Request:**
```json
{
    "success": false,
    "error": "Trường title là bắt buộc"
}
```

**404 Not Found:**
```json
{
    "success": false,
    "error": "Đơn hàng không tồn tại"
}
```

**500 Internal Server Error:**
```json
{
    "success": false,
    "error": "Lỗi server: Database connection failed"
}
```

### Checklist troubleshooting

1. **Kiểm tra URL:** Đảm bảo URL đúng và server đang chạy
2. **Kiểm tra Headers:** Content-Type phải là `application/json`
3. **Kiểm tra JSON:** Đảm bảo JSON syntax đúng
4. **Kiểm tra Required Fields:** Tất cả các trường bắt buộc phải có giá trị
5. **Kiểm tra Data Types:** Đảm bảo kiểu dữ liệu đúng (số, chuỗi, boolean)
6. **Kiểm tra Foreign Keys:** ID của các đối tượng liên quan phải tồn tại

### Ví dụ test nhanh với cURL

**Tạo công ty:**
```bash
curl -X POST http://127.0.0.1:8000/companies/api/create/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Test Company",
    "company_type": "customer",
    "tax_code": "TEST123",
    "address": "Test Address"
  }'
```

**Tạo đơn hàng:**
```bash
curl -X POST http://127.0.0.1:8000/orders/api/create/ \
  -H "Content-Type: application/json" \
  -d '{
    "order_type": "domestic_sale",
    "company_id": 1,
    "products": [{"product_id": 1, "quantity": 1, "unit_price": 100000}]
  }'
```

---

**Lưu ý quan trọng:**
- Tất cả các timestamp đều theo format ISO 8601 (UTC)
- Các trường tiền tệ đều tính bằng VND
- ID của các đối tượng liên quan (company_id, product_id, etc.) phải tồn tại trong database
- Một số API có thể yêu cầu authentication tùy thuộc vào cấu hình hệ thống

---

## API Xuất nhập kho (Stock Movement)

### 1. Tạo phiếu xuất nhập kho đơn lẻ

**Endpoint:** `POST /inventory/api/movements/create/`

**Request Body:**
```json
{
    "movement_type": "inbound",
    "warehouse_id": 1,
    "product_id": 1,
    "quantity": 100,
    "unit_cost": 50000,
    "reference_type": "purchase_order",
    "reference_id": "PO001",
    "notes": "Nhập hàng từ nhà cung cấp ABC"
}
```

**Loại phiếu (movement_type):**
- `inbound`: Nhập kho
- `outbound`: Xuất kho  
- `transfer`: Chuyển kho
- `adjustment`: Điều chỉnh tồn kho
- `damaged`: Hàng hỏng
- `expired`: Hàng hết hạn

**Response thành công:**
```json
{
    "success": true,
    "message": "Tạo phiếu xuất nhập kho thành công",
    "data": {
        "id": 1,
        "movement_type": "inbound",
        "movement_type_display": "Nhập kho",
        "warehouse": {
            "id": 1,
            "name": "Kho Hà Nội",
            "code": "HN001"
        },
        "product": {
            "id": 1,
            "name": "Sản phẩm A",
            "code": "SP001"
        },
        "quantity": 100.0,
        "unit_cost": 50000.0,
        "reference_type": "purchase_order",
        "reference_id": "PO001",
        "notes": "Nhập hàng từ nhà cung cấp ABC",
        "current_stock": 150.0,
        "created_at": "2024-01-01T10:00:00Z"
    }
}
```

### 2. Lấy danh sách phiếu xuất nhập kho

**Endpoint:** `GET /inventory/api/movements/list/`

**Query Parameters:**
- `page`: Số trang (mặc định: 1)
- `per_page`: Số items mỗi trang (mặc định: 10, tối đa: 100)
- `movement_type`: Lọc theo loại phiếu
- `warehouse_id`: Lọc theo kho
- `product_id`: Lọc theo sản phẩm

**Ví dụ URL:**
```
GET /inventory/api/movements/list/?movement_type=inbound&warehouse_id=1&page=1&per_page=20
```

### 3. Xem chi tiết phiếu xuất nhập kho

**Endpoint:** `GET /inventory/api/movements/{movement_id}/`

**Ví dụ:**
```
GET /inventory/api/movements/1/
```

**Response:**
```json
{
    "success": true,
    "data": {
        "id": 1,
        "movement_type": "inbound",
        "movement_type_display": "Nhập kho",
        "warehouse": {
            "id": 1,
            "name": "Kho Hà Nội",
            "code": "HN001"
        },
        "product": {
            "id": 1,
            "name": "Sản phẩm A",
            "code": "SP001"
        },
        "quantity": 100.0,
        "unit_cost": 50000.0,
        "reference_type": "purchase_order",
        "reference_id": "PO001",
        "notes": "Nhập hàng từ nhà cung cấp ABC",
        "created_by": "admin",
        "created_at": "2024-01-01T10:00:00Z",
        "updated_at": "2024-01-01T10:00:00Z"
    }
}
```

### 4. Workflow xuất nhập kho hoàn chỉnh

**Bước 1: Tạo kho**
```bash
curl -X POST http://127.0.0.1:8000/inventory/api/warehouses/create/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Kho Test",
    "code": "TEST001",
    "address": "123 Test Street",
    "is_active": true
  }'
```

**Bước 2: Nhập hàng vào kho**
```bash
curl -X POST http://127.0.0.1:8000/inventory/api/movements/create/ \
  -H "Content-Type: application/json" \
  -d '{
    "movement_type": "inbound",
    "warehouse_id": 1,
    "product_id": 1,
    "quantity": 100,
    "unit_cost": 50000,
    "notes": "Nhập hàng đầu tiên"
  }'
```

**Bước 3: Xuất hàng từ kho**
```bash
curl -X POST http://127.0.0.1:8000/inventory/api/movements/create/ \
  -H "Content-Type: application/json" \
  -d '{
    "movement_type": "outbound",
    "warehouse_id": 1,
    "product_id": 1,
    "quantity": 20,
    "reference_type": "sales_order",
    "reference_id": "SO001",
    "notes": "Xuất hàng cho đơn SO001"
  }'
```

**Bước 4: Xem lịch sử xuất nhập**
```bash
curl http://127.0.0.1:8000/inventory/api/movements/list/?warehouse_id=1&product_id=1
```
