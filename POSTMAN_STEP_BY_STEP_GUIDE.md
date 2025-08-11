# Hướng dẫn từng bước tạo Customer, Warehouse, News trong Postman

## 📋 Mục lục
1. [Thiết lập Postman](#thiết-lập-postman)
2. [Tạo Customer (Khách hàng)](#tạo-customer-khách-hàng)
3. [Tạo Warehouse (Kho hàng)](#tạo-warehouse-kho-hàng)
4. [Tạo News (Tin tức)](#tạo-news-tin-tức)
5. [Kiểm tra kết quả](#kiểm-tra-kết-quả)
6. [Xử lý lỗi thường gặp](#xử-lý-lỗi-thường-gặp)

---

## 1. Thiết lập Postman

### Bước 1: Mở Postman
- Khởi động ứng dụng Postman trên máy tính
- Tạo một Collection mới tên "Django API Tests"

### Bước 2: Thiết lập Environment (Tùy chọn)
- Vào Settings > Environment
- Tạo environment mới: "Local Django"
- Thêm biến: `base_url` = `http://127.0.0.1:8000`

### Bước 3: Đảm bảo Django server đang chạy
```bash
cd d:\IT\summer-2\QLDA
python manage.py runserver
```

---

## 2. Tạo Customer (Khách hàng)

### 🎯 Bước 1: Tạo request mới trong Postman

1. **Click "New Request"** trong Collection "Django API Tests"
2. **Đặt tên**: "Create Customer"
3. **Chọn method**: `POST`
4. **URL**: `http://127.0.0.1:8000/companies/api/create/`

### 🎯 Bước 2: Thiết lập Headers

Trong tab **Headers**, thêm:
```
Key: Content-Type    | Value: application/json
Key: Accept          | Value: application/json
```

### 🎯 Bước 3: Chuẩn bị dữ liệu Body

Chọn tab **Body** > **raw** > **JSON**, sau đó dán nội dung:

```json
{
    "name": "Công ty TNHH Trái Cây Sạch Việt Nam",
    "company_type": "customer",
    "tax_code": "0123456789",
    "address": "123 Đường Lê Văn Việt, Quận 9, TP.HCM",
    "phone": "028-12345678",
    "email": "info@traicaysach.vn",
    "website": "https://traicaysach.vn",
    "contact_person": "Nguyễn Văn An",
    "contact_phone": "0987654321",
    "contact_email": "nguyen.an@traicaysach.vn",
    "bank_name": "Ngân hàng TMCP Á Châu (ACB)",
    "bank_account": "1234567890",
    "import_license": "",
    "export_license": "XK-2024-001",
    "is_active": true
}
```

### 🎯 Bước 4: Gửi request

1. **Click "Send"**
2. **Kiểm tra Status**: Phải là `200 OK`
3. **Xem Response**:

```json
{
    "success": true,
    "message": "Tạo công ty thành công",
    "data": {
        "id": 1,
        "name": "Công ty TNHH Trái Cây Sạch Việt Nam",
        "company_type": "customer",
        "tax_code": "0123456789",
        "address": "123 Đường Lê Văn Việt, Quận 9, TP.HCM",
        "phone": "028-12345678",
        "email": "info@traicaysach.vn",
        "website": "https://traicaysach.vn",
        "contact_person": "Nguyễn Văn An",
        "contact_phone": "0987654321",
        "contact_email": "nguyen.an@traicaysach.vn",
        "bank_name": "Ngân hàng TMCP Á Châu (ACB)",
        "bank_account": "1234567890",
        "import_license": "",
        "export_license": "XK-2024-001",
        "is_active": true,
        "created_at": "2024-08-09T14:30:00.000Z",
        "updated_at": "2024-08-09T14:30:00.000Z"
    }
}
```

### 🎯 Bước 5: Lưu Customer ID

**Quan trọng**: Ghi nhớ `id` từ response (ví dụ: `1`) để sử dụng cho các API khác.

---

## 3. Tạo Warehouse (Kho hàng)

### 🎯 Bước 1: Tạo request mới

1. **Click "New Request"** 
2. **Đặt tên**: "Create Warehouse"
3. **Method**: `POST`
4. **URL**: `http://127.0.0.1:8000/inventory/api/warehouses/create/`

### 🎯 Bước 2: Thiết lập Headers

```
Key: Content-Type    | Value: application/json
Key: Accept          | Value: application/json
```

### 🎯 Bước 3: Chuẩn bị Body

```json
{
    "name": "Kho Lạnh Trái Cây Quận 7",
    "code": "WH-Q7-001",
    "address": "789 Đường Nguyễn Thị Thập, Quận 7, TP.HCM",
    "manager_id": null,
    "capacity": 500.75,
    "is_active": true
}
```

**Lưu ý về các trường:**
- `name`: Tên kho (bắt buộc, không trùng)
- `code`: Mã kho (bắt buộc, không trùng)
- `address`: Địa chỉ kho (bắt buộc)
- `manager_id`: ID người quản lý (có thể null)
- `capacity`: Sức chứa tính bằng tấn (bắt buộc)
- `is_active`: Trạng thái hoạt động (mặc định true)

### 🎯 Bước 4: Gửi request

**Click "Send"** và kiểm tra response:

```json
{
    "success": true,
    "message": "Tạo kho thành công",
    "data": {
        "id": 1,
        "name": "Kho Lạnh Trái Cây Quận 7",
        "code": "WH-Q7-001",
        "address": "789 Đường Nguyễn Thị Thập, Quận 7, TP.HCM",
        "manager_id": null,
        "manager_name": null,
        "capacity": 500.75,
        "is_active": true,
        "created_at": "2024-08-09T14:35:00.000Z"
    }
}
```

---

## 4. Tạo News (Tin tức)

### 🎯 Bước 1: Tạo danh mục tin tức trước (nếu cần)

Kiểm tra danh mục có sẵn:
- **Method**: `GET`
- **URL**: `http://127.0.0.1:8000/news/api/categories/`

### 🎯 Bước 2: Tạo request tin tức

1. **Tạo request mới**: "Create News"
2. **Method**: `POST`
3. **URL**: `http://127.0.0.1:8000/news/api/create/`

### 🎯 Bước 3: Headers

```
Key: Content-Type    | Value: application/json
Key: Accept          | Value: application/json
```

### 🎯 Bước 4: Body - Tin tức thông thường

```json
{
    "title": "Giá trái cây xuất khẩu tăng mạnh trong tháng 8",
    "summary": "Thị trường trái cây xuất khẩu ghi nhận mức tăng trưởng ấn tượng 25% so với cùng kỳ năm trước, đặc biệt là thanh long và xoài.",
    "content": "<h2>Tình hình thị trường</h2><p>Theo thống kê từ Bộ Nông nghiệp và Phát triển nông thôn, xuất khẩu trái cây Việt Nam trong tháng 8/2025 đạt kim ngạch 800 triệu USD, tăng 25% so với cùng kỳ năm 2024.</p><h3>Các loại trái cây chủ lực:</h3><ul><li>Thanh long: 300 triệu USD (+30%)</li><li>Xoài: 200 triệu USD (+22%)</li><li>Vải thiều: 150 triệu USD (+18%)</li><li>Bưởi: 100 triệu USD (+15%)</li></ul><p>Trung Quốc vẫn là thị trường nhập khẩu lớn nhất với 60% tổng kim ngạch.</p>",
    "category_id": 1,
    "news_type": "market",
    "status": "published",
    "priority": "high",
    "expiry_date": null,
    "is_featured": true,
    "is_active": true
}
```

### 🎯 Bước 5: Body - Thông báo quy định

```json
{
    "title": "Thông báo: Quy định mới về chứng nhận xuất xứ trái cây",
    "summary": "Từ ngày 15/8/2025, các doanh nghiệp xuất khẩu trái cây cần tuân thủ quy định mới về chứng nhận xuất xứ và truy xuất nguồn gốc.",
    "content": "<div class='alert alert-warning'><strong>Thông báo quan trọng!</strong></div><h2>Quy định mới có hiệu lực từ 15/8/2025</h2><h3>Các yêu cầu chính:</h3><ol><li><strong>Chứng nhận xuất xứ:</strong> Tất cả lô hàng trái cây xuất khẩu phải có giấy chứng nhận xuất xứ từ cơ quan có thẩm quyền.</li><li><strong>Mã truy xuất:</strong> Mỗi sản phẩm phải có mã QR code để truy xuất nguồn gốc.</li><li><strong>Hồ sơ vệ sinh:</strong> Cung cấp đầy đủ hồ sơ về quy trình canh tác và bảo quản.</li></ol><h3>Thủ tục thực hiện:</h3><p>Doanh nghiệp cần nộp hồ sơ tại Chi cục Trồng trọt và Bảo vệ thực vật địa phương trước 7 ngày xuất hàng.</p><p><strong>Liên hệ hỗ trợ:</strong> Hotline 1900-1234</p>",
    "category_id": 1,
    "news_type": "regulation",
    "status": "published",
    "priority": "urgent",
    "expiry_date": "2025-12-31",
    "is_featured": true,
    "is_active": true
}
```

### 🎯 Bước 6: Giải thích các trường

**Các giá trị hợp lệ:**

| Trường | Giá trị hợp lệ | Mô tả |
|--------|----------------|--------|
| `news_type` | `internal`, `industry`, `system`, `regulation`, `market` | Loại tin tức |
| `status` | `draft`, `published`, `archived` | Trạng thái |
| `priority` | `low`, `normal`, `high`, `urgent` | Độ ưu tiên |

### 🎯 Bước 7: Gửi request

**Response thành công:**

```json
{
    "success": true,
    "message": "Tạo tin tức thành công",
    "data": {
        "id": 1,
        "title": "Giá trái cây xuất khẩu tăng mạnh trong tháng 8",
        "slug": "gia-trai-cay-xuat-khau-tang-manh-trong-thang-8",
        "summary": "Thị trường trái cây xuất khẩu ghi nhận mức tăng trưởng ấn tượng...",
        "content": "<h2>Tình hình thị trường</h2>...",
        "category_id": 1,
        "category_name": "Thị trường",
        "news_type": "market",
        "status": "published",
        "priority": "high",
        "author_id": 1,
        "author_name": "Admin User",
        "publish_date": "2024-08-09T14:40:00.000Z",
        "expiry_date": null,
        "is_featured": true,
        "is_active": true,
        "views_count": 0,
        "created_at": "2024-08-09T14:40:00.000Z",
        "updated_at": "2024-08-09T14:40:00.000Z"
    }
}
```

---

## 5. Kiểm tra kết quả

### 🔍 Kiểm tra Customer đã tạo

**Request**: `GET http://127.0.0.1:8000/companies/api/list/?type=customer`

### 🔍 Kiểm tra Warehouse đã tạo

**Request**: `GET http://127.0.0.1:8000/inventory/api/warehouses/list/`

### 🔍 Kiểm tra News đã tạo

**Request**: `GET http://127.0.0.1:8000/news/api/list/?status=published`

### 🔍 Xem chi tiết từng đối tượng

- Customer: `GET http://127.0.0.1:8000/companies/api/{id}/`
- Warehouse: `GET http://127.0.0.1:8000/inventory/api/warehouses/{id}/`
- News: `GET http://127.0.0.1:8000/news/api/{id}/`

---

## 6. Xử lý lỗi thường gặp

### ❌ Lỗi 400 - Bad Request

**Lỗi thiếu trường bắt buộc:**
```json
{
    "success": false,
    "error": "Trường name là bắt buộc"
}
```
**Giải pháp**: Kiểm tra lại tất cả các trường có dấu `*` (bắt buộc)

**Lỗi trùng lặp:**
```json
{
    "success": false,
    "error": "Mã số thuế đã tồn tại"
}
```
**Giải pháp**: Thay đổi giá trị `tax_code` hoặc `code`

### ❌ Lỗi 404 - Not Found

**Lỗi category không tồn tại:**
```json
{
    "success": false,
    "error": "Danh mục tin tức không tồn tại"
}
```
**Giải pháp**: 
1. Kiểm tra `category_id` có đúng không
2. Tạo category trước bằng Django Admin

### ❌ Lỗi 500 - Server Error

**Lỗi kết nối database:**
```json
{
    "success": false,
    "error": "Lỗi server: Database connection failed"
}
```
**Giải pháp**: 
1. Kiểm tra Django server có đang chạy
2. Kiểm tra database connection
3. Xem log server để biết chi tiết

### 🔧 Các bước debug

1. **Kiểm tra URL**: Đảm bảo đúng endpoint
2. **Kiểm tra Headers**: Content-Type phải là application/json
3. **Validate JSON**: Sử dụng JSON validator để kiểm tra syntax
4. **Kiểm tra server logs**: Xem terminal Django để biết lỗi chi tiết
5. **Test với cURL**: Thử với cURL để loại trừ lỗi từ Postman

---

## 📖 Tài liệu tham khảo nhanh

### Customer Fields (Required: *)
- `name*`: Tên công ty
- `company_type*`: customer, supplier, partner, our_company
- `tax_code*`: Mã số thuế (unique)
- `address*`: Địa chỉ

### Warehouse Fields (Required: *)
- `name*`: Tên kho (unique)
- `code*`: Mã kho (unique)
- `address*`: Địa chỉ
- `capacity*`: Sức chứa (số thực)

### News Fields (Required: *)
- `title*`: Tiêu đề
- `summary*`: Tóm tắt
- `content*`: Nội dung HTML
- `category_id*`: ID danh mục
- `news_type*`: internal, industry, system, regulation, market

**Chúc bạn thành công với việc test API!** 🎉
