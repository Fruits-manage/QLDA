from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator

User = get_user_model()

class CustomerProfile(models.Model):
    """Model cho hồ sơ khách hàng - chỉ dành cho người dân bình thường"""
    
    MEMBERSHIP_CHOICES = [
        ('bronze', 'Đồng'),
        ('silver', 'Bạc'), 
        ('gold', 'Vàng'),
        ('platinum', 'Bạch kim'),
    ]
    
    # Liên kết với User
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='customer_portal_profile')
    
    # Thông tin cơ bản
    customer_code = models.CharField(max_length=20, unique=True, verbose_name="Mã khách hàng")
    
    # Thông tin liên hệ
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Số điện thoại phải có định dạng: '+999999999'. Tối đa 15 chữ số.")
    phone = models.CharField(validators=[phone_regex], max_length=17, verbose_name="Số điện thoại")
    
    # Địa chỉ giao hàng
    province = models.CharField(max_length=100, verbose_name="Tỉnh/Thành phố")
    district = models.CharField(max_length=100, verbose_name="Quận/Huyện")  
    ward = models.CharField(max_length=100, verbose_name="Phường/Xã")
    address = models.TextField(verbose_name="Địa chỉ chi tiết")
    
    # Thành viên và ưu đãi
    membership_level = models.CharField(max_length=10, choices=MEMBERSHIP_CHOICES, default='bronze', verbose_name="Cấp thành viên")
    points = models.IntegerField(default=0, verbose_name="Điểm tích lũy")
    
    # Sở thích
    preferred_products = models.TextField(blank=True, verbose_name="Sản phẩm ưa thích")
    preferred_payment_method = models.CharField(max_length=50, blank=True, verbose_name="Phương thức thanh toán ưa thích")
    
    # Thống kê
    total_orders = models.IntegerField(default=0, verbose_name="Tổng số đơn hàng")
    total_spent = models.DecimalField(max_digits=15, decimal_places=2, default=0, verbose_name="Tổng chi tiêu")
    
    # Trạng thái
    is_verified = models.BooleanField(default=False, verbose_name="Đã xác minh")
    is_vip = models.BooleanField(default=False, verbose_name="Khách hàng VIP")
    
    # Thời gian
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Ngày tạo")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Ngày cập nhật")
    
    class Meta:
        verbose_name = "Hồ sơ khách hàng"
        verbose_name_plural = "Hồ sơ khách hàng"
        
    def __str__(self):
        return f"{self.customer_code} - {self.user.get_full_name()}"
        
    def save(self, *args, **kwargs):
        if not self.customer_code:
            # Tự động tạo mã khách hàng
            last_customer = CustomerProfile.objects.order_by('-id').first()
            if last_customer and last_customer.customer_code:
                try:
                    number = int(last_customer.customer_code.split('C')[-1]) + 1
                except:
                    number = 1
            else:
                number = 1
            self.customer_code = f"C{number:06d}"
        super().save(*args, **kwargs)

class CustomerAddress(models.Model):
    """Địa chỉ giao hàng của khách hàng"""
    customer = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE, related_name='addresses')
    label = models.CharField(max_length=50, verbose_name="Nhãn địa chỉ", help_text="VD: Nhà riêng, Công ty")
    recipient_name = models.CharField(max_length=200, verbose_name="Tên người nhận")
    phone = models.CharField(max_length=17, verbose_name="Số điện thoại người nhận")
    province = models.CharField(max_length=100, verbose_name="Tỉnh/Thành phố")
    district = models.CharField(max_length=100, verbose_name="Quận/Huyện")
    ward = models.CharField(max_length=100, verbose_name="Phường/Xã")
    address = models.TextField(verbose_name="Địa chỉ chi tiết")
    is_default = models.BooleanField(default=False, verbose_name="Địa chỉ mặc định")
    
    class Meta:
        verbose_name = "Địa chỉ giao hàng"
        verbose_name_plural = "Địa chỉ giao hàng"
        
    def __str__(self):
        return f"{self.label} - {self.recipient_name}"

class CustomerWishlist(models.Model):
    """Danh sách yêu thích của khách hàng"""
    customer = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE, related_name='wishlist')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True, verbose_name="Ngày thêm")
    
    class Meta:
        verbose_name = "Sản phẩm yêu thích"
        verbose_name_plural = "Sản phẩm yêu thích"
        unique_together = ['customer', 'product']
        
    def __str__(self):
        return f"{self.customer.user.get_full_name()} - {self.product.name}"

class CustomerReview(models.Model):
    """Đánh giá sản phẩm của khách hàng"""
    customer = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE, related_name='reviews')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='reviews')
    order = models.ForeignKey('orders.Order', on_delete=models.CASCADE, null=True, blank=True)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="Đánh giá")
    comment = models.TextField(verbose_name="Bình luận")
    is_verified_purchase = models.BooleanField(default=False, verbose_name="Đã mua hàng")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Ngày đánh giá")
    
    class Meta:
        verbose_name = "Đánh giá sản phẩm"
        verbose_name_plural = "Đánh giá sản phẩm"
        unique_together = ['customer', 'product', 'order']
        
    def __str__(self):
        return f"{self.customer.user.get_full_name()} - {self.product.name} ({self.rating}★)"
