# HƯỚNG DẪN SỬ DỤNG HỆ THỐNG QUẢN LÝ XUẤT NHẬP KHẨU TRÁI CÂY

## 1. TỔNG QUAN HỆ THỐNG

### Mục đích
Hệ thống quản lý toàn bộ quy trình xuất nhập khẩu trái cây từ việc quản lý sản phẩm, đơn hàng, kho bãi, thanh toán đến các thủ tục hải quan.

### Các chức năng chính:
- **Dashboard**: Trang tổng quan với biểu đồ, thống kê
- **Quản lý tài khoản**: Phân quyền người dùng theo vai trò
- **Quản lý công ty**: Thông tin đối tác, nhà cung cấp, khách hàng
- **Quản lý sản phẩm**: Danh mục trái cây, thông số kỹ thuật
- **Quản lý kho**: Tồn kho, nhập xuất, kiểm kê
- **Quản lý đơn hàng**: Tạo, theo dõi đơn hàng xuất nhập khẩu
- **Quản lý thanh toán**: Ghi nhận thanh toán, lịch thanh toán
- **Thủ tục xuất nhập khẩu**: Tờ khai hải quan, giấy tờ CO/CQ
- **Tin tức**: Thông báo nội bộ, tin tức ngành
- **Nhật ký hoạt động**: Theo dõi mọi thao tác trong hệ thống

## 2. HƯỚNG DẪN ĐĂNG NHẬP

### Bước 1: Truy cập hệ thống
- Mở trình duyệt web và truy cập: `http://localhost:8000`
- Hệ thống sẽ tự động chuyển hướng đến trang đăng nhập

### Bước 2: Đăng nhập Admin
- URL Admin: `http://localhost:8000/admin/`
- Sử dụng tài khoản superuser đã tạo

### Bước 3: Truy cập Dashboard
- Sau khi đăng nhập, truy cập: `http://localhost:8000/dashboard/`

## 3. HƯỚNG DẪN SỬ DỤNG CÁC MODULE

### 3.1 Dashboard
- **Trang chính**: Hiển thị thống kê tổng quan
  - Tổng số đơn hàng, sản phẩm, công ty
  - Doanh thu tổng
  - Biểu đồ doanh thu 12 tháng
  - Đơn hàng gần đây
  - Cảnh báo tồn kho thấp
  - Thanh toán chờ xử lý

### 3.2 Quản lý Công ty
- **Thêm công ty mới**: Nhập thông tin cơ bản, liên hệ, ngân hàng
- **Phân loại**: Công ty chúng tôi, nhà cung cấp, khách hàng, đối tác
- **Quản lý tài liệu**: Upload giấy phép kinh doanh, xuất nhập khẩu

### 3.3 Quản lý Sản phẩm
- **Thêm sản phẩm**: Mã SP, tên, danh mục, đơn vị tính
- **Thông tin kỹ thuật**: Xuất xứ, chất lượng, hạn sử dụng
- **Giá cả**: Giá vốn, bán, xuất khẩu
- **Hình ảnh**: Upload nhiều ảnh, chọn ảnh chính
- **Mã HS**: Mã hàng hóa xuất nhập khẩu

### 3.4 Quản lý Kho
- **Quản lý kho**: Tạo các kho, phân công quản lý
- **Tồn kho**: Xem tình trạng tồn kho theo sản phẩm/kho
- **Biến động**: Theo dõi nhập/xuất/chuyển kho
- **Kiểm kê**: Lập phiếu kiểm kê, so sánh thực tế

### 3.5 Quản lý Đơn hàng
- **Tạo đơn hàng**: Chọn loại (xuất/nhập khẩu), công ty
- **Chi tiết đơn**: Thêm sản phẩm, số lượng, giá
- **Theo dõi**: Cập nhật trạng thái vận chuyển
- **Tài liệu**: Upload hợp đồng, invoice, vận đơn

### 3.6 Quản lý Thanh toán
- **Lịch thanh toán**: Chia nhỏ thanh toán theo đợt
- **Ghi nhận thanh toán**: Nhập thông tin chuyển khoản
- **Theo dõi**: Trạng thái thanh toán, quá hạn
- **Báo cáo**: Dòng tiền, công nợ

### 3.7 Thủ tục Xuất nhập khẩu
- **Tờ khai hải quan**: Lập tờ khai, nộp cơ quan hải quan
- **Giấy tờ CO/CQ**: Quản lý chứng chỉ xuất xứ, chất lượng
- **Vận đơn**: B/L, AWB, vận đơn đường bộ
- **Theo dõi**: Trạng thái thông quan

### 3.8 Tin tức & Thông báo
- **Tin nội bộ**: Thông báo công ty
- **Tin ngành**: Cập nhật thị trường, quy định
- **Thông báo hệ thống**: Bảo trì, cập nhật

### 3.9 Nhật ký Hoạt động
- **Theo dõi**: Mọi thao tác tạo/sửa/xóa
- **Bảo mật**: Phát hiện hoạt động bất thường
- **Báo cáo**: Xuất nhật ký theo thời gian

## 4. QUY TRÌNH NGHIỆP VỤ XUẤT KHẨU

### Bước 1: Nhận đơn hàng
1. Tạo đơn hàng xuất khẩu
2. Nhập thông tin khách hàng, sản phẩm
3. Xác nhận giá, điều khoản

### Bước 2: Chuẩn bị hàng
1. Kiểm tra tồn kho
2. Đặt hàng nhà cung cấp (nếu thiếu)
3. Kiểm tra chất lượng

### Bước 3: Thủ tục xuất khẩu
1. Lập tờ khai hải quan
2. Xin giấy chứng nhận CO/CQ
3. Làm thủ tục kiểm dịch

### Bước 4: Vận chuyển
1. Đóng gói, dán nhãn
2. Vận chuyển đến cảng
3. Lên tàu/máy bay

### Bước 5: Thanh toán
1. Xuất hóa đơn
2. Gửi L/C hoặc nhận TT
3. Theo dõi thanh toán

## 5. QUY TRÌNH NGHIỆP VỤ NHẬP KHẨU

### Bước 1: Đặt hàng
1. Tạo đơn hàng nhập khẩu  
2. Gửi PO cho nhà cung cấp
3. Xác nhận đơn hàng

### Bước 2: Theo dõi hàng
1. Nhận invoice, packing list
2. Theo dõi vận chuyển
3. Chuẩn bị thủ tục nhập khẩu

### Bước 3: Thủ tục nhập khẩu
1. Lập tờ khai nhập khẩu
2. Nộp thuế, phí
3. Làm thủ tục thông quan

### Bước 4: Nhận hàng
1. Nhận hàng tại cảng
2. Vận chuyển về kho
3. Kiểm tra, nhập kho

### Bước 5: Thanh toán
1. Thanh toán cho NCC
2. Cập nhật công nợ
3. Lưu trữ chứng từ

## 6. PHÂN QUYỀN NGƯỜI DÙNG

### Admin: Toàn quyền hệ thống
- Quản lý tài khoản, phân quyền
- Cấu hình hệ thống
- Xem mọi báo cáo

### Manager: Quản lý nghiệp vụ
- Duyệt đơn hàng, thanh toán
- Xem báo cáo tổng hợp
- Quản lý nhân viên

### Staff: Nhân viên nghiệp vụ
- Tạo đơn hàng, cập nhật trạng thái
- Quản lý kho, sản phẩm
- Xử lý thủ tục hải quan

### Accountant: Kế toán
- Quản lý thanh toán
- Xuất báo cáo tài chính
- Theo dõi công nợ

## 7. LƯU Ý QUAN TRỌNG

### Bảo mật
- Thay đổi mật khẩu định kỳ
- Không chia sẻ tài khoản
- Đăng xuất sau khi sử dụng

### Sao lưu dữ liệu
- Hệ thống tự động backup hàng ngày
- Xuất dữ liệu quan trọng định kỳ

### Hỗ trợ kỹ thuật
- Liên hệ IT khi gặp lỗi
- Báo cáo lỗi qua hệ thống ticket

## 8. THÔNG TIN LIÊN HỆ

- **Hỗ trợ kỹ thuật**: it-support@company.com
- **Đào tạo sử dụng**: training@company.com
- **Hotline**: 1900-xxxx
