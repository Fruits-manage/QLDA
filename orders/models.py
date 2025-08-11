from django.db import models
from django.core.validators import MinValueValidator
from products.models import Product
from companies.models import Company
from accounts.models import User

class Order(models.Model):
    """Đơn hàng"""
    ORDER_TYPE_CHOICES = [
        ('export_sale', 'Xuất khẩu'),
        ('import_purchase', 'Nhập khẩu'),
        ('domestic_sale', 'Bán nội địa'),
        ('domestic_purchase', 'Mua nội địa'),
    ]
    
    STATUS_CHOICES = [
        ('draft', 'Nháp'),
        ('confirmed', 'Đã xác nhận'),
        ('processing', 'Đang xử lý'),
        ('shipped', 'Đã giao hàng'),
        ('delivered', 'Đã nhận hàng'),
        ('completed', 'Hoàn thành'),
        ('cancelled', 'Đã hủy'),
    ]
    
    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Chờ thanh toán'),
        ('partial', 'Thanh toán một phần'),
        ('paid', 'Đã thanh toán'),
        ('overdue', 'Quá hạn'),
    ]
    
    order_number = models.CharField(max_length=50, unique=True, verbose_name="Số đơn hàng")
    order_type = models.CharField(max_length=20, choices=ORDER_TYPE_CHOICES, verbose_name="Loại đơn hàng")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="Công ty")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft', verbose_name="Trạng thái")
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='pending', verbose_name="Trạng thái thanh toán")
    
    # Ngày tháng
    order_date = models.DateTimeField(auto_now_add=True, verbose_name="Ngày đặt hàng")
    delivery_date = models.DateField(blank=True, null=True, verbose_name="Ngày giao hàng")
    expected_delivery = models.DateField(blank=True, null=True, verbose_name="Ngày giao dự kiến")
    
    # Thông tin giao hàng
    shipping_address = models.TextField(verbose_name="Địa chỉ giao hàng")
    shipping_contact = models.CharField(max_length=100, blank=True, verbose_name="Người nhận")
    shipping_phone = models.CharField(max_length=15, blank=True, verbose_name="SĐT người nhận")
    
    # Thông tin tài chính
    subtotal = models.DecimalField(max_digits=15, decimal_places=2, default=0, verbose_name="Tổng tiền hàng")
    tax_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0, verbose_name="Tiền thuế")
    shipping_cost = models.DecimalField(max_digits=15, decimal_places=2, default=0, verbose_name="Phí vận chuyển")
    discount_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0, verbose_name="Giảm giá")
    total_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0, verbose_name="Tổng cộng")
    
    # Thông tin khác
    notes = models.TextField(blank=True, verbose_name="Ghi chú")
    internal_notes = models.TextField(blank=True, verbose_name="Ghi chú nội bộ")
    
    # Thông tin người tạo/cập nhật
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_orders', verbose_name="Người tạo")
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='updated_orders', verbose_name="Người cập nhật")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Ngày tạo")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Ngày cập nhật")
    
    class Meta:
        verbose_name = "Đơn hàng"
        verbose_name_plural = "Đơn hàng"
        ordering = ['-created_at']
        
    def __str__(self):
        return f"{self.order_number} - {self.company.name}"
        
    def save(self, *args, **kwargs):
        if not self.order_number:
            # Tự động tạo số đơn hàng
            prefix = self.order_type.upper()[:2]
            last_order = Order.objects.filter(order_type=self.order_type).order_by('-id').first()
            if last_order:
                number = int(last_order.order_number.split('-')[-1]) + 1
            else:
                number = 1
            self.order_number = f"{prefix}-{number:06d}"
        super().save(*args, **kwargs)

class OrderDetail(models.Model):
    """Chi tiết đơn hàng"""
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='details', verbose_name="Đơn hàng")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Sản phẩm")
    quantity = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], verbose_name="Số lượng")
    unit_price = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(0)], verbose_name="Đơn giá")
    total_price = models.DecimalField(max_digits=15, decimal_places=2, default=0, verbose_name="Thành tiền")
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0, verbose_name="Thuế suất (%)")
    discount_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0, verbose_name="Giảm giá (%)")
    notes = models.TextField(blank=True, verbose_name="Ghi chú")
    
    class Meta:
        verbose_name = "Chi tiết đơn hàng"
        verbose_name_plural = "Chi tiết đơn hàng"
        unique_together = ['order', 'product']
        
    def save(self, *args, **kwargs):
        self.total_price = self.quantity * self.unit_price
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.order.order_number} - {self.product.name}"

class OrderStatusHistory(models.Model):
    """Lịch sử thay đổi trạng thái đơn hàng"""
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='status_history')
    from_status = models.CharField(max_length=20, blank=True, verbose_name="Trạng thái cũ")
    to_status = models.CharField(max_length=20, verbose_name="Trạng thái mới")
    notes = models.TextField(blank=True, verbose_name="Ghi chú")
    changed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="Người thay đổi")
    changed_at = models.DateTimeField(auto_now_add=True, verbose_name="Thời gian thay đổi")
    
    class Meta:
        verbose_name = "Lịch sử trạng thái"
        verbose_name_plural = "Lịch sử trạng thái"
        ordering = ['-changed_at']
        
    def __str__(self):
        return f"{self.order.order_number}: {self.from_status} → {self.to_status}"

class OrderDocument(models.Model):
    """Tài liệu đơn hàng"""
    DOCUMENT_TYPE_CHOICES = [
        ('contract', 'Hợp đồng'),
        ('invoice', 'Hóa đơn'),
        ('packing_list', 'Danh sách đóng gói'),
        ('bill_of_lading', 'Vận đơn'),
        ('certificate', 'Chứng chỉ'),
        ('other', 'Khác'),
    ]
    
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='documents')
    document_type = models.CharField(max_length=20, choices=DOCUMENT_TYPE_CHOICES, verbose_name="Loại tài liệu")
    title = models.CharField(max_length=200, verbose_name="Tiêu đề")
    file = models.FileField(upload_to='order_documents/', verbose_name="File")
    notes = models.TextField(blank=True, verbose_name="Ghi chú")
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="Người tải lên")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Ngày tải lên")
    
    class Meta:
        verbose_name = "Tài liệu đơn hàng"
        verbose_name_plural = "Tài liệu đơn hàng"
        
    def __str__(self):
        return f"{self.order.order_number} - {self.title}"
