from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator

class User(AbstractUser):
    """Custom User model cho Farmer"""
    ROLE_CHOICES = [
        ('farmer', 'Nông dân'),
        ('farm_manager', 'Quản lý nông trại'),
        ('cooperative_member', 'Thành viên hợp tác xã'),
    ]
    
    phone = models.CharField(max_length=15, blank=True, null=True, verbose_name="Số điện thoại")
    address = models.TextField(blank=True, null=True, verbose_name="Địa chỉ")
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='farmer', verbose_name="Vai trò")
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name="Ảnh đại diện")
    is_active_employee = models.BooleanField(default=True, verbose_name="Đang hoạt động")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Ngày tạo")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Ngày cập nhật")
    
    class Meta:
        verbose_name = "Nông dân"
        verbose_name_plural = "Nông dân"
        
    def __str__(self):
        return f"{self.get_full_name()} ({self.username})"
        
    def get_role_display_vietnamese(self):
        """Hiển thị vai trò bằng tiếng Việt"""
        return dict(self.ROLE_CHOICES).get(self.role, self.role)


class FarmerProfile(models.Model):
    """Hồ sơ nông dân - thay thế cho Company model"""
    FARMER_TYPE_CHOICES = [
        ('individual', 'Cá nhân'),
        ('cooperative', 'Hợp tác xã'),
        ('small_farm', 'Nông trại nhỏ'),
        ('organic_farm', 'Nông trại hữu cơ'),
    ]
    
    CERTIFICATION_CHOICES = [
        ('none', 'Chưa có'),
        ('organic', 'Hữu cơ'),
        ('vietgap', 'VietGAP'),
        ('globalgap', 'GlobalGAP'),
    ]
    
    # Liên kết với User
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='farmer_profile')
    
    # Thông tin nông trại
    farm_name = models.CharField(max_length=100, verbose_name="Tên nông trại")
    farmer_code = models.CharField(max_length=20, unique=True, verbose_name="Mã nông dân")
    farmer_type = models.CharField(max_length=20, choices=FARMER_TYPE_CHOICES, default='individual')
    
    # Thông tin liên hệ
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Số điện thoại không hợp lệ")
    phone = models.CharField(validators=[phone_regex], max_length=17, verbose_name="Số điện thoại")
    email = models.EmailField(verbose_name="Email")
    
    # Địa chỉ chi tiết
    farm_address = models.TextField(verbose_name="Địa chỉ nông trại")
    province = models.CharField(max_length=50, verbose_name="Tỉnh/Thành phố")
    district = models.CharField(max_length=50, verbose_name="Quận/Huyện")
    ward = models.CharField(max_length=50, verbose_name="Phường/Xã")
    
    # Thông tin canh tác
    farm_area = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Diện tích (ha)")
    main_products = models.TextField(verbose_name="Sản phẩm chính", help_text="Liệt kê các loại trái cây chính")
    certification = models.CharField(max_length=20, choices=CERTIFICATION_CHOICES, default='none')
    
    # Thông tin khác
    experience_years = models.PositiveIntegerField(default=0, verbose_name="Số năm kinh nghiệm")
    established_date = models.DateField(verbose_name="Ngày thành lập/bắt đầu")
    is_verified = models.BooleanField(default=False, verbose_name="Đã xác thực")
    is_active = models.BooleanField(default=True, verbose_name="Đang hoạt động")
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Hồ sơ nông dân"
        verbose_name_plural = "Hồ sơ nông dân"
        ordering = ['-created_at']
        
    def __str__(self):
        return f"{self.farm_name} - {self.user.get_full_name()}"

class UserProfile(models.Model):
    """Thông tin mở rộng của User"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    employee_id = models.CharField(max_length=10, unique=True, verbose_name="Mã nhân viên")
    department = models.CharField(max_length=100, blank=True, verbose_name="Phòng ban")
    position = models.CharField(max_length=100, blank=True, verbose_name="Chức vụ")
    hire_date = models.DateField(blank=True, null=True, verbose_name="Ngày vào làm")
    salary = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name="Lương")
    
    class Meta:
        verbose_name = "Hồ sơ nhân viên"
        verbose_name_plural = "Hồ sơ nhân viên"
        
    def __str__(self):
        return f"Profile of {self.user.get_full_name()}"
