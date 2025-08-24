from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator

User = get_user_model()

class FarmerProfile(models.Model):
    """Model cho thông tin nông dân"""
    FARMER_TYPE_CHOICES = [
        ('individual', 'Cá nhân'),
        ('cooperative', 'Hợp tác xã'),
        ('company', 'Doanh nghiệp'),
    ]
    
    CERTIFICATION_CHOICES = [
        ('organic', 'Hữu cơ'),
        ('vietgap', 'VietGAP'),
        ('globalgap', 'GlobalGAP'),
        ('haccp', 'HACCP'),
        ('iso', 'ISO'),
        ('none', 'Không có'),
    ]
    
    # Liên kết với User
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='farmer_profile')
    
    # Thông tin cơ bản
    farmer_code = models.CharField(max_length=20, unique=True, verbose_name="Mã nông dân")
    farmer_type = models.CharField(max_length=20, choices=FARMER_TYPE_CHOICES, verbose_name="Loại hình")
    
    # Thông tin liên hệ
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Số điện thoại phải có định dạng: '+999999999'. Tối đa 15 chữ số.")
    phone = models.CharField(validators=[phone_regex], max_length=17, verbose_name="Số điện thoại")
    
    # Địa chỉ và vùng canh tác
    province = models.CharField(max_length=100, verbose_name="Tỉnh/Thành phố")
    district = models.CharField(max_length=100, verbose_name="Quận/Huyện")
    ward = models.CharField(max_length=100, verbose_name="Phường/Xã")
    address = models.TextField(verbose_name="Địa chỉ chi tiết")
    farming_region = models.CharField(max_length=200, verbose_name="Vùng canh tác")
    
    # Thông tin canh tác
    total_farm_area = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Tổng diện tích canh tác (ha)")
    active_farm_area = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Diện tích đang canh tác (ha)")
    farming_experience = models.IntegerField(validators=[MinValueValidator(0)], default=0, verbose_name="Kinh nghiệm canh tác (năm)")
    main_crops = models.TextField(verbose_name="Cây trồng chính")
    
    # Chứng nhận và chất lượng
    certifications = models.CharField(max_length=20, choices=CERTIFICATION_CHOICES, default='none', verbose_name="Chứng nhận")
    certification_number = models.CharField(max_length=100, blank=True, verbose_name="Số chứng nhận")
    certification_expiry = models.DateField(blank=True, null=True, verbose_name="Ngày hết hạn chứng nhận")
    
    # Thông tin ngân hàng
    bank_name = models.CharField(max_length=100, blank=True, verbose_name="Tên ngân hàng")
    bank_account = models.CharField(max_length=50, blank=True, verbose_name="Số tài khoản")
    account_holder = models.CharField(max_length=100, blank=True, verbose_name="Tên chủ tài khoản")
    
    # Thông tin thuế (nếu có)
    tax_code = models.CharField(max_length=20, blank=True, unique=True, null=True, verbose_name="Mã số thuế")
    
    # Đánh giá và xếp hạng
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0, 
                               validators=[MinValueValidator(0), MaxValueValidator(5)], verbose_name="Đánh giá")
    total_reviews = models.IntegerField(default=0, verbose_name="Tổng số đánh giá")
    
    # Trạng thái
    is_verified = models.BooleanField(default=False, verbose_name="Đã xác minh")
    is_active = models.BooleanField(default=True, verbose_name="Đang hoạt động")
    is_featured = models.BooleanField(default=False, verbose_name="Nông dân nổi bật")
    
    # Thời gian
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Ngày tạo")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Ngày cập nhật")
    
    class Meta:
        verbose_name = "Hồ sơ nông dân"
        verbose_name_plural = "Hồ sơ nông dân"
        
    def __str__(self):
        return f"{self.farmer_code} - {self.user.get_full_name()}"
        
    def save(self, *args, **kwargs):
        if not self.farmer_code:
            # Tự động tạo mã nông dân
            last_farmer = FarmerProfile.objects.order_by('-id').first()
            if last_farmer and last_farmer.farmer_code:
                try:
                    number = int(last_farmer.farmer_code.split('F')[-1]) + 1
                except:
                    number = 1
            else:
                number = 1
            self.farmer_code = f"F{number:06d}"
        super().save(*args, **kwargs)

class FarmingArea(models.Model):
    """Khu vực canh tác của nông dân"""
    farmer = models.ForeignKey(FarmerProfile, on_delete=models.CASCADE, related_name='farming_areas')
    area_name = models.CharField(max_length=200, verbose_name="Tên khu vực")
    area_size = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Diện tích (ha)")
    soil_type = models.CharField(max_length=100, verbose_name="Loại đất")
    water_source = models.CharField(max_length=100, verbose_name="Nguồn nước")
    coordinates = models.CharField(max_length=100, blank=True, verbose_name="Tọa độ GPS")
    description = models.TextField(blank=True, verbose_name="Mô tả chi tiết")
    
    class Meta:
        verbose_name = "Khu vực canh tác"
        verbose_name_plural = "Khu vực canh tác"
        
    def __str__(self):
        return f"{self.farmer.farmer_code} - {self.area_name}"

class CropProduct(models.Model):
    """Sản phẩm nông nghiệp của nông dân"""
    PRODUCT_STATUS_CHOICES = [
        ('planning', 'Đang lên kế hoạch'),
        ('growing', 'Đang trồng'),
        ('harvesting', 'Đang thu hoạch'),
        ('available', 'Có sẵn'),
        ('sold_out', 'Đã bán hết'),
    ]
    
    farmer = models.ForeignKey(FarmerProfile, on_delete=models.CASCADE, related_name='crop_products')
    farming_area = models.ForeignKey(FarmingArea, on_delete=models.CASCADE, related_name='crop_products')
    product_name = models.CharField(max_length=200, verbose_name="Tên sản phẩm")
    variety = models.CharField(max_length=100, verbose_name="Giống cây")
    planted_area = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Diện tích trồng (ha)")
    planting_date = models.DateField(verbose_name="Ngày gieo trồng")
    expected_harvest_date = models.DateField(verbose_name="Ngày dự kiến thu hoạch")
    expected_yield = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Sản lượng dự kiến (tấn)")
    actual_yield = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Sản lượng thực tế (tấn)")
    price_per_kg = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Giá bán (VND/kg)")
    status = models.CharField(max_length=20, choices=PRODUCT_STATUS_CHOICES, default='growing', verbose_name="Trạng thái")
    description = models.TextField(blank=True, verbose_name="Mô tả sản phẩm")
    
    class Meta:
        verbose_name = "Sản phẩm nông nghiệp"
        verbose_name_plural = "Sản phẩm nông nghiệp"
        
    def __str__(self):
        return f"{self.farmer.farmer_code} - {self.product_name} ({self.variety})"
