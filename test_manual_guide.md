# HƯỚNG DẪN TEST MANUAL TOÀN BỘ HỆ THỐNG CRUD
# Fruit Management System - Complete Manual Testing Guide

## 🚀 CHUẨN BỊ TEST

### 1. Khởi động server
```bash
cd d:\IT\summer-2\QLDA
python manage.py runserver
```
Server sẽ chạy tại: http://127.0.0.1:8000/

### 2. Tạo superuser (nếu chưa có)
```bash
python manage.py createsuperuser
```

---

## 📋 CHECKLIST TEST TOÀN BỘ HỆ THỐNG

### ✅ 1. PRODUCTS MODULE (Sản phẩm)

#### Test Products CRUD:
- [ ] **CREATE**: Vào `/products/create/`
  - Điền đầy đủ thông tin sản phẩm
  - Kiểm tra validation form
  - Bấm Save và kiểm tra redirect
  - Kiểm tra thông báo thành công

- [ ] **READ**: Vào `/products/`
  - Kiểm tra hiển thị danh sách sản phẩm
  - Test pagination (nếu có nhiều sản phẩm)
  - Test search/filter (nếu có)
  - Click vào detail từng sản phẩm

- [ ] **UPDATE**: Click "Edit" trên sản phẩm
  - Form phải load đúng dữ liệu hiện tại
  - Thay đổi vài field và save
  - Kiểm tra dữ liệu đã update chưa
  - Kiểm tra thông báo thành công

- [ ] **DELETE**: Click "Delete" trên sản phẩm
  - Hiển thị confirmation page
  - Confirm delete
  - Kiểm tra sản phẩm đã biến mất khỏi list

#### Test Categories & Units:
- [ ] Tạo category mới: `/admin/products/category/`
- [ ] Tạo unit mới: `/admin/products/unit/`
- [ ] Kiểm tra trong form create product có hiển thị đúng

---

### ✅ 2. COMPANIES MODULE (Công ty)

#### Test Companies CRUD:
- [ ] **CREATE**: Vào `/companies/create/`
  - Điền thông tin công ty đầy đủ
  - Test validation (tax_code, email, phone)
  - Save và kiểm tra redirect
  - Kiểm tra thông báo thành công

- [ ] **READ**: Vào `/companies/`
  - Kiểm tra danh sách công ty
  - Click detail từng công ty
  - Kiểm tra thông tin hiển thị đúng

- [ ] **UPDATE**: Click "Edit" công ty
  - Form load đúng dữ liệu
  - Sửa tên công ty và thông tin khác
  - Save và kiểm tra update thành công

- [ ] **DELETE**: Click "Delete" công ty
  - Confirm và kiểm tra đã xóa

---

### ✅ 3. INVENTORY MODULE (Kho hàng)

#### Test Warehouses CRUD:
- [ ] **CREATE**: Vào `/inventory/warehouses/create/`
  - Điền thông tin kho: name, code, address, capacity
  - Chọn manager
  - Save và kiểm tra

- [ ] **READ**: Vào `/inventory/warehouses/`
  - Xem danh sách kho
  - Click detail từng kho

- [ ] **UPDATE**: Edit warehouse
  - Sửa thông tin kho
  - Save và kiểm tra

#### Test Stock CRUD:
- [ ] **CREATE**: Vào `/inventory/stock/create/`
  - Chọn product và warehouse
  - Nhập quantity, min/max levels
  - Save và kiểm tra

- [ ] **READ**: Vào `/inventory/stock/`
  - Xem tồn kho từng sản phẩm
  - Kiểm tra số liệu đúng

- [ ] **UPDATE**: Edit stock
  - Sửa quantity
  - Kiểm tra cập nhật thành công

#### Test Stock Movements:
- [ ] **CREATE**: Vào `/inventory/movements/create/`
  - Chọn warehouse, product
  - Chọn loại movement: IN/OUT
  - Nhập quantity, unit_cost
  - Save và kiểm tra stock tự động update

- [ ] **READ**: Vào `/inventory/movements/`
  - Xem lịch sử xuất nhập kho
  - Kiểm tra thông tin movement

---

### ✅ 4. ORDERS MODULE (Đơn hàng)

#### Test Orders CRUD:
- [ ] **CREATE**: Vào `/orders/create/`
  - Chọn company (khách hàng)
  - Nhập delivery_date
  - Chọn priority, payment method
  - **QUAN TRỌNG**: Kiểm tra field order_date không có trong form
  - Add products vào order
  - Save và kiểm tra

- [ ] **READ**: Vào `/orders/`
  - Xem danh sách đơn hàng
  - Click detail order
  - Kiểm tra order details (sản phẩm trong đơn)

- [ ] **UPDATE**: Edit order
  - Sửa thông tin đơn hàng
  - Sửa products trong đơn
  - Save và kiểm tra

#### Test Order Details:
- [ ] Trong order detail, kiểm tra:
  - Danh sách sản phẩm đúng
  - Quantity, price đúng
  - Total amount tính đúng

---

### ✅ 5. NEWS MODULE (Tin tức)

#### Test News CRUD:
- [ ] **CREATE**: Vào `/news/create/`
  - Nhập title, summary, content
  - Chọn category, news_type
  - Chọn status: draft/published
  - Save và kiểm tra

- [ ] **READ**: Vào `/news/`
  - Xem danh sách tin tức
  - Click detail tin tức
  - Kiểm tra hiển thị đúng

- [ ] **UPDATE**: Edit news
  - Sửa title, content
  - Đổi status từ draft thành published
  - Save và kiểm tra

- [ ] **DELETE**: Delete news
  - Confirm và kiểm tra

#### Test News Categories:
- [ ] Tạo news category: `/admin/news/newscategory/`
- [ ] Kiểm tra trong form tạo news có category mới

---

### ✅ 6. MANAGEMENT MODULE (Quản lý)

#### Test Employees CRUD:
- [ ] **CREATE**: Vào `/management/employees/create/`
  - Điền thông tin nhân viên đầy đủ
  - employee_id, name, email, phone
  - department, position, salary
  - Save và kiểm tra

- [ ] **READ**: Vào `/management/employees/`
  - Xem danh sách nhân viên
  - Click detail nhân viên

- [ ] **UPDATE**: Edit employee
  - Sửa salary, position
  - Save và kiểm tra

#### Test Customers CRUD:
- [ ] **CREATE**: Vào `/management/customers/create/`
  - Điền customer_code, name
  - customer_type, contact info
  - credit_limit, payment_terms
  - Save và kiểm tra

- [ ] **READ**: Vào `/management/customers/`
  - Xem danh sách khách hàng
  - Click detail khách hàng

- [ ] **UPDATE**: Edit customer
  - Sửa thông tin khách hàng
  - Save và kiểm tra

---

### ✅ 7. AUTHENTICATION & ADMIN

#### Test Authentication:
- [ ] Logout và thử truy cập trang yêu cầu login
- [ ] Login lại với user/password
- [ ] Kiểm tra redirect sau login thành công

#### Test Admin Interface:
- [ ] Vào `/admin/` với superuser
- [ ] Kiểm tra tất cả models có hiển thị
- [ ] Test CRUD từng model trong admin
- [ ] Kiểm tra admin của từng app:
  - [ ] Products admin
  - [ ] Companies admin  
  - [ ] Orders admin
  - [ ] Inventory admin
  - [ ] News admin
  - [ ] Management admin

---

### ✅ 8. DASHBOARD & NAVIGATION

#### Test Dashboard:
- [ ] Vào trang chủ `/`
- [ ] Kiểm tra các widgets/stats hiển thị
- [ ] Kiểm tra links đến các module

#### Test Navigation:
- [ ] Kiểm tra menu navigation
- [ ] Test breadcrumbs
- [ ] Test back buttons
- [ ] Test tất cả internal links

---

### ✅ 9. DATA INTEGRITY & RELATIONSHIPS

#### Test Foreign Key Relationships:
- [ ] Tạo Order với Product -> Kiểm tra relationship
- [ ] Tạo Stock với Product + Warehouse -> Kiểm tra relationship  
- [ ] Delete Product có được dùng trong Order -> Kiểm tra cascade/protect
- [ ] Delete Warehouse có Stock -> Kiểm tra cascade/protect

#### Test Data Validation:
- [ ] Nhập email sai format -> Kiểm tra validation
- [ ] Nhập phone sai format -> Kiểm tra validation
- [ ] Nhập quantity âm -> Kiểm tra validation
- [ ] Để trống required fields -> Kiểm tra validation

---

### ✅ 10. PERFORMANCE & ERROR HANDLING

#### Test Error Pages:
- [ ] Truy cập URL không tồn tại -> Kiểm tra 404 page
- [ ] Truy cập without permission -> Kiểm tra 403 page
- [ ] Submit invalid data -> Kiểm tra error messages

#### Test Performance:
- [ ] Load trang với nhiều data -> Kiểm tra tốc độ
- [ ] Test pagination với large dataset
- [ ] Test search/filter performance

---

## 🚨 COMMON ISSUES TO CHECK

### 1. Template Issues:
- [ ] Kiểm tra không có template not found errors
- [ ] Kiểm tra CSS/JS files load đúng
- [ ] Kiểm tra responsive design trên mobile

### 2. Database Issues:
- [ ] Kiểm tra migration applied đầy đủ
- [ ] Kiểm tra không có orphaned records
- [ ] Kiểm tra foreign key constraints

### 3. Form Issues:
- [ ] Tất cả forms submit thành công
- [ ] Validation messages hiển thị đúng
- [ ] Success messages hiển thị sau save

### 4. URL Issues:
- [ ] Tất cả internal links working
- [ ] URL patterns match views correctly
- [ ] No reverse URL errors

---

## 📊 TEST COMPLETION CHECKLIST

| Module | Create | Read | Update | Delete | Admin | Status |
|--------|--------|------|--------|--------|-------|--------|
| Products | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| Companies | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| Inventory | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| Orders | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| News | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| Management | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |

## 🎯 FINAL VERIFICATION

- [ ] Tất cả CRUD operations working
- [ ] Không có 404/500 errors
- [ ] Tất cả forms validation working  
- [ ] Database relationships intact
- [ ] Admin interface functional
- [ ] Authentication working
- [ ] User experience smooth

---

**💡 TIP**: Run automated tests trước khi manual test:
```bash
python test_quick_crud.py
python test_complete_crud.py
```

**🐛 BUG REPORT**: Nếu phát hiện lỗi, ghi lại:
1. Steps to reproduce
2. Expected behavior
3. Actual behavior  
4. Error messages
5. Browser/environment info
