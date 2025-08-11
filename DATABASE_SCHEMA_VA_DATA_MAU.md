# DANH SÁCH CÁC BẢNG VÀ TRƯỜNG DỮ LIỆU - ĐỂ TẠO DATA MẪU

## 1. APP ACCOUNTS

### Bảng: accounts_user
```
- id (tự động)
- username (varchar 150) - Tên đăng nhập
- email (email) - Email
- first_name (varchar 150) - Họ
- last_name (varchar 30) - Tên  
- phone (varchar 15) - Số điện thoại
- address (text) - Địa chỉ
- role (varchar 20) - Vai trò: admin, manager, staff, accountant
- avatar (file upload) - Ảnh đại diện
- is_active_employee (boolean) - Đang làm việc
- password (hashed) - Mật khẩu
- is_staff (boolean) - Là nhân viên
- is_active (boolean) - Tài khoản hoạt động
- date_joined (datetime) - Ngày tham gia
- created_at (datetime) - Ngày tạo
- updated_at (datetime) - Ngày cập nhật
```

### Bảng: accounts_userprofile
```
- id (tự động)
- user_id (foreign key) - Liên kết User
- employee_id (varchar 10) - Mã nhân viên
- department (varchar 100) - Phòng ban
- position (varchar 100) - Chức vụ
- hire_date (date) - Ngày vào làm
- salary (decimal 12,2) - Lương
```

## 2. APP COMPANIES

### Bảng: companies_company
```
- id (tự động)
- name (varchar 200) - Tên công ty
- company_type (varchar 20) - Loại: our_company, supplier, customer, partner
- tax_code (varchar 20) - Mã số thuế
- address (text) - Địa chỉ
- phone (varchar 15) - Số điện thoại
- email (email) - Email
- website (url) - Website
- bank_name (varchar 100) - Tên ngân hàng
- bank_account (varchar 50) - Số tài khoản
- contact_person (varchar 100) - Người liên hệ
- contact_phone (varchar 15) - SĐT người liên hệ
- contact_email (email) - Email người liên hệ
- import_license (varchar 50) - Giấy phép nhập khẩu
- export_license (varchar 50) - Giấy phép xuất khẩu
- is_active (boolean) - Đang hoạt động
- created_at (datetime) - Ngày tạo
- updated_at (datetime) - Ngày cập nhật
```

### Bảng: companies_companydocument
```
- id (tự động)
- company_id (foreign key) - Liên kết Company
- document_type (varchar 20) - Loại: business_license, tax_certificate, import_license, export_license, other
- title (varchar 200) - Tiêu đề
- file (file upload) - File tài liệu
- expiry_date (date) - Ngày hết hạn
- notes (text) - Ghi chú
- uploaded_at (datetime) - Ngày tải lên
```

## 3. APP PRODUCTS

### Bảng: products_category
```
- id (tự động)
- name (varchar 100) - Tên danh mục
- description (text) - Mô tả
- image (file upload) - Hình ảnh
- is_active (boolean) - Đang hoạt động
- created_at (datetime) - Ngày tạo
```

### Bảng: products_unit
```
- id (tự động)
- name (varchar 50) - Tên đơn vị
- symbol (varchar 10) - Ký hiệu
- description (text) - Mô tả
```

### Bảng: products_product
```
- id (tự động)
- code (varchar 20) - Mã sản phẩm
- name (varchar 200) - Tên sản phẩm
- category_id (foreign key) - Liên kết Category
- unit_id (foreign key) - Liên kết Unit
- description (text) - Mô tả
- image (file upload) - Hình ảnh
- origin (varchar 100) - Vùng xuất xứ
- origin_country (varchar 100) - Quốc gia (mặc định: Việt Nam)
- quality_grade (varchar 1) - Phân loại: A, B, C
- cost_price (decimal 12,2) - Giá vốn
- selling_price (decimal 12,2) - Giá bán
- export_price (decimal 12,2) - Giá xuất khẩu
- shelf_life_days (integer) - Hạn sử dụng (ngày)
- storage_temperature_min (decimal 5,2) - Nhiệt độ bảo quản tối thiểu
- storage_temperature_max (decimal 5,2) - Nhiệt độ bảo quản tối đa
- humidity_requirement (integer) - Độ ẩm yêu cầu (%)
- hs_code (varchar 20) - Mã HS
- tax_rate (decimal 5,2) - Thuế suất (%)
- is_active (boolean) - Đang kinh doanh
- created_at (datetime) - Ngày tạo
- updated_at (datetime) - Ngày cập nhật
```

## 4. APP INVENTORY

### Bảng: inventory_warehouse
```
- id (tự động)
- name (varchar 100) - Tên kho
- code (varchar 20) - Mã kho
- address (text) - Địa chỉ
- manager_id (foreign key) - Quản lý kho
- capacity (decimal 10,2) - Sức chứa (tấn)
- is_active (boolean) - Đang hoạt động
- created_at (datetime) - Ngày tạo
```

### Bảng: inventory_inventorystock
```
- id (tự động)
- warehouse_id (foreign key) - Liên kết Warehouse
- product_id (foreign key) - Liên kết Product
- quantity (decimal 10,2) - Số lượng tồn
- reserved_quantity (decimal 10,2) - Số lượng đặt trước
- min_stock_level (decimal 10,2) - Mức tồn kho tối thiểu
- max_stock_level (decimal 10,2) - Mức tồn kho tối đa
- last_updated (datetime) - Cập nhật cuối
```

### Bảng: inventory_stockmovement
```
- id (tự động)
- warehouse_id (foreign key) - Liên kết Warehouse
- product_id (foreign key) - Liên kết Product
- movement_type (varchar 20) - Loại: inbound, outbound, transfer, adjustment, damaged, expired
- quantity (decimal 10,2) - Số lượng
- unit_cost (decimal 12,2) - Đơn giá
- reference_type (varchar 50) - Loại tham chiếu
- reference_id (integer) - ID tham chiếu
- notes (text) - Ghi chú
- created_by_id (foreign key) - Người tạo
- created_at (datetime) - Ngày tạo
```

## 5. APP ORDERS

### Bảng: orders_order
```
- id (tự động)
- order_number (varchar 50) - Số đơn hàng
- order_type (varchar 20) - Loại: export, import, domestic_sale, domestic_purchase
- company_id (foreign key) - Liên kết Company
- status (varchar 20) - Trạng thái: draft, confirmed, processing, shipped, delivered, completed, cancelled
- payment_status (varchar 20) - Trạng thái thanh toán: pending, partial, paid, overdue
- order_date (datetime) - Ngày đặt hàng
- delivery_date (date) - Ngày giao hàng
- expected_delivery (date) - Ngày giao dự kiến
- shipping_address (text) - Địa chỉ giao hàng
- shipping_contact (varchar 100) - Người nhận
- shipping_phone (varchar 15) - SĐT người nhận
- subtotal (decimal 15,2) - Tổng tiền hàng
- tax_amount (decimal 15,2) - Tiền thuế
- shipping_cost (decimal 15,2) - Phí vận chuyển
- discount_amount (decimal 15,2) - Giảm giá
- total_amount (decimal 15,2) - Tổng cộng
- notes (text) - Ghi chú
- internal_notes (text) - Ghi chú nội bộ
- created_by_id (foreign key) - Người tạo
- updated_by_id (foreign key) - Người cập nhật
- created_at (datetime) - Ngày tạo
- updated_at (datetime) - Ngày cập nhật
```

### Bảng: orders_orderdetail
```
- id (tự động)
- order_id (foreign key) - Liên kết Order
- product_id (foreign key) - Liên kết Product
- quantity (decimal 10,2) - Số lượng
- unit_price (decimal 12,2) - Đơn giá
- total_price (decimal 15,2) - Thành tiền
- tax_rate (decimal 5,2) - Thuế suất (%)
- discount_rate (decimal 5,2) - Giảm giá (%)
- notes (text) - Ghi chú
```

## 6. APP PAYMENTS

### Bảng: payments_payment
```
- id (tự động)
- payment_code (varchar 50) - Mã thanh toán
- payment_type (varchar 20) - Loại: inbound, outbound
- order_id (foreign key) - Liên kết Order
- company_id (foreign key) - Liên kết Company
- amount (decimal 15,2) - Số tiền
- payment_method (varchar 20) - Phương thức: cash, bank_transfer, check, credit_card, letter_of_credit, other
- status (varchar 20) - Trạng thái: pending, completed, failed, cancelled
- payment_date (date) - Ngày thanh toán
- due_date (date) - Ngày đến hạn
- bank_name (varchar 100) - Tên ngân hàng
- bank_account (varchar 50) - Số tài khoản
- transaction_reference (varchar 100) - Mã giao dịch
- notes (text) - Ghi chú
- exchange_rate (decimal 10,4) - Tỷ giá
- currency (varchar 3) - Tiền tệ (mặc định: VND)
- created_by_id (foreign key) - Người tạo
- approved_by_id (foreign key) - Người duyệt
- created_at (datetime) - Ngày tạo
- updated_at (datetime) - Ngày cập nhật
```

### Bảng: payments_exchangerate
```
- id (tự động)
- from_currency (varchar 3) - Từ tiền tệ
- to_currency (varchar 3) - Sang tiền tệ
- rate (decimal 10,4) - Tỷ giá
- effective_date (date) - Ngày hiệu lực
- notes (text) - Ghi chú
- created_by_id (foreign key) - Người tạo
- created_at (datetime) - Ngày tạo
```

## 7. APP IMPORT_EXPORT

### Bảng: import_export_customsdeclaration
```
- id (tự động)
- order_id (foreign key) - Liên kết Order
- declaration_number (varchar 50) - Số tờ khai
- declaration_type (varchar 20) - Loại: import, export
- status (varchar 20) - Trạng thái: draft, submitted, processing, cleared, rejected
- customs_office (varchar 200) - Cơ quan hải quan
- port_of_entry (varchar 200) - Cửa khẩu
- declaration_date (date) - Ngày khai báo
- submission_date (date) - Ngày nộp
- clearance_date (date) - Ngày thông quan
- declared_value (decimal 15,2) - Giá trị khai báo
- currency (varchar 3) - Tiền tệ
- customs_duty (decimal 15,2) - Thuế quan
- vat_amount (decimal 15,2) - Thuế VAT
- other_fees (decimal 15,2) - Phí khác
- total_tax (decimal 15,2) - Tổng thuế phí
- notes (text) - Ghi chú
- created_by_id (foreign key) - Người tạo
- created_at (datetime) - Ngày tạo
- updated_at (datetime) - Ngày cập nhật
```

### Bảng: import_export_importexportdocument
```
- id (tự động)
- order_id (foreign key) - Liên kết Order
- document_type (varchar 30) - Loại: customs_declaration, commercial_invoice, packing_list, bill_of_lading, certificate_of_origin, quality_certificate, phytosanitary_certificate, insurance_certificate, letter_of_credit, inspection_certificate, other
- document_number (varchar 100) - Số tài liệu
- title (varchar 200) - Tiêu đề
- issue_date (date) - Ngày phát hành
- expiry_date (date) - Ngày hết hạn
- issuing_authority (varchar 200) - Cơ quan cấp
- status (varchar 20) - Trạng thái: draft, submitted, approved, rejected, expired
- submission_date (date) - Ngày nộp
- approval_date (date) - Ngày duyệt
- file (file upload) - File tài liệu
- notes (text) - Ghi chú
- created_by_id (foreign key) - Người tạo
- approved_by_id (foreign key) - Người duyệt
- created_at (datetime) - Ngày tạo
- updated_at (datetime) - Ngày cập nhật
```

## 8. APP NEWS

### Bảng: news_newscategory
```
- id (tự động)
- name (varchar 100) - Tên danh mục
- description (text) - Mô tả
- color (varchar 7) - Màu sắc (mặc định: #007bff)
- is_active (boolean) - Đang hoạt động
- created_at (datetime) - Ngày tạo
```

### Bảng: news_news
```
- id (tự động)
- title (varchar 200) - Tiêu đề
- slug (varchar 200) - Slug
- summary (text 500) - Tóm tắt
- content (text) - Nội dung
- category_id (foreign key) - Liên kết NewsCategory
- news_type (varchar 20) - Loại: internal, industry, system, regulation, market
- priority (varchar 20) - Độ ưu tiên: low, normal, high, urgent
- status (varchar 20) - Trạng thái: draft, published, archived
- is_featured (boolean) - Tin nổi bật
- is_pinned (boolean) - Ghim tin
- featured_image (file upload) - Hình ảnh đại diện
- publish_date (datetime) - Ngày xuất bản
- expire_date (datetime) - Ngày hết hạn
- view_count (integer) - Lượt xem
- author_id (foreign key) - Tác giả
- created_at (datetime) - Ngày tạo
- updated_at (datetime) - Ngày cập nhật
```

### Bảng: news_systemnotification
```
- id (tự động)
- title (varchar 200) - Tiêu đề
- message (text) - Nội dung
- notification_type (varchar 20) - Loại: info, warning, error, success, maintenance
- target_roles (varchar 200) - Vai trò nhận (cách nhau bằng dấu phẩy)
- is_global (boolean) - Thông báo toàn hệ thống
- is_active (boolean) - Đang hoạt động
- start_date (datetime) - Thời gian bắt đầu
- end_date (datetime) - Thời gian kết thúc
- created_by_id (foreign key) - Người tạo
- created_at (datetime) - Ngày tạo
```

## 9. APP ACTIVITY_LOGS

### Bảng: activity_logs_activitylog
```
- id (tự động)
- user_id (foreign key) - Người thực hiện
- action (varchar 20) - Hành động: create, update, delete, view, login, logout, export, import, approve, reject, cancel, restore, other
- description (text) - Mô tả
- severity (varchar 20) - Mức độ: low, medium, high, critical
- content_type_id (foreign key) - Loại đối tượng
- object_id (integer) - ID đối tượng
- ip_address (IP) - Địa chỉ IP
- user_agent (text) - User Agent
- session_key (varchar 40) - Session Key
- old_values (JSON) - Giá trị cũ
- new_values (JSON) - Giá trị mới
- extra_data (JSON) - Dữ liệu bổ sung
- timestamp (datetime) - Thời gian
```

### Bảng: activity_logs_loginhistory
```
- id (tự động)
- user_id (foreign key) - Người dùng
- login_time (datetime) - Thời gian đăng nhập
- logout_time (datetime) - Thời gian đăng xuất
- ip_address (IP) - Địa chỉ IP
- user_agent (text) - User Agent
- session_key (varchar 40) - Session Key
- is_successful (boolean) - Đăng nhập thành công
- failure_reason (varchar 200) - Lý do thất bại
```

---

## HƯỚNG DẪN TẠO DATA MẪU

### 1. Thứ tự tạo data (quan trọng):
1. **User & UserProfile** - Tạo tài khoản admin và nhân viên
2. **NewsCategory** - Danh mục tin tức
3. **Company** - Công ty, nhà cung cấp, khách hàng
4. **Category & Unit** - Danh mục và đơn vị tính sản phẩm
5. **Product** - Sản phẩm trái cây
6. **Warehouse** - Kho hàng
7. **InventoryStock** - Tồn kho
8. **Order & OrderDetail** - Đơn hàng và chi tiết
9. **Payment** - Thanh toán
10. **CustomsDeclaration** - Tờ khai hải quan
11. **News** - Tin tức
12. **ActivityLog** - Nhật ký hoạt động

### 2. Gợi ý data mẫu:

#### Companies:
- Công ty xuất khẩu trái cây Việt Nam
- Tập đoàn ABC (khách hàng Mỹ)  
- Công ty DEF (nhà cung cấp trái cây)

#### Products:
- Thanh long ruột đỏ (Dragon fruit)
- Xoài cát Hòa Lộc (Mango)
- Nhãn longan (Longan)
- Vải thiều (Lychee)
- Chôm chôm (Rambutan)

#### Order Types:
- Xuất khẩu thanh long sang Mỹ
- Nhập khẩu táo từ Mỹ
- Bán nội địa xoài

### 3. Tools để tạo data:
- Django Admin Panel
- Django Shell
- Fixture files (JSON)
- Custom management commands
