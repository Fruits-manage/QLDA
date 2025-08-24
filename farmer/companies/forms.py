from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import FarmerProfile, FarmingArea, CropProduct

class FarmerRegistrationForm(UserCreationForm):
    """Form đăng ký nông dân"""
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email của bạn'
    }))
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Tên'
    }))
    last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control', 
        'placeholder': 'Họ'
    }))
    phone = forms.CharField(max_length=17, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Số điện thoại'
    }))
    farmer_type = forms.ChoiceField(
        choices=FarmerProfile.FARMER_TYPE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tên đăng nhập'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Mật khẩu'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Xác nhận mật khẩu'})

class FarmerProfileForm(forms.ModelForm):
    """Form cập nhật thông tin nông dân"""
    class Meta:
        model = FarmerProfile
        fields = [
            'farmer_type', 'phone', 'province', 'district', 'ward', 'address',
            'farming_region', 'total_farm_area', 'active_farm_area', 'farming_experience',
            'main_crops', 'certifications', 'certification_number', 'certification_expiry',
            'bank_name', 'bank_account', 'account_holder', 'tax_code'
        ]
        widgets = {
            'farmer_type': forms.Select(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Số điện thoại'}),
            'province': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tỉnh/Thành phố'}),
            'district': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Quận/Huyện'}),
            'ward': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phường/Xã'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Địa chỉ chi tiết'}),
            'farming_region': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Vùng canh tác'}),
            'total_farm_area': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'Tổng diện tích (ha)'}),
            'active_farm_area': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'Diện tích đang canh tác (ha)'}),
            'farming_experience': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Số năm kinh nghiệm'}),
            'main_crops': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Mô tả các loại cây trồng chính'}),
            'certifications': forms.Select(attrs={'class': 'form-control'}),
            'certification_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Số chứng nhận'}),
            'certification_expiry': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'bank_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tên ngân hàng'}),
            'bank_account': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Số tài khoản'}),
            'account_holder': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tên chủ tài khoản'}),
            'tax_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mã số thuế (nếu có)'}),
        }

class FarmingAreaForm(forms.ModelForm):
    """Form thêm/sửa khu vực canh tác"""
    class Meta:
        model = FarmingArea
        fields = ['area_name', 'area_size', 'soil_type', 'water_source', 'coordinates', 'description']
        widgets = {
            'area_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tên khu vực'}),
            'area_size': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'Diện tích (ha)'}),
            'soil_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Loại đất'}),
            'water_source': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nguồn nước'}),
            'coordinates': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tọa độ GPS (nếu có)'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Mô tả chi tiết'}),
        }

class CropProductForm(forms.ModelForm):
    """Form thêm/sửa sản phẩm nông nghiệp"""
    class Meta:
        model = CropProduct
        fields = [
            'farming_area', 'product_name', 'variety', 'planted_area', 'planting_date',
            'expected_harvest_date', 'expected_yield', 'actual_yield', 'price_per_kg',
            'status', 'description'
        ]
        widgets = {
            'farming_area': forms.Select(attrs={'class': 'form-control'}),
            'product_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tên sản phẩm'}),
            'variety': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Giống cây'}),
            'planted_area': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'Diện tích trồng (ha)'}),
            'planting_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'expected_harvest_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'expected_yield': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'Sản lượng dự kiến (tấn)'}),
            'actual_yield': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'Sản lượng thực tế (tấn)'}),
            'price_per_kg': forms.NumberInput(attrs={'class': 'form-control', 'step': '1000', 'placeholder': 'Giá bán (VND/kg)'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Mô tả sản phẩm'}),
        }
    
    def __init__(self, *args, **kwargs):
        farmer = kwargs.pop('farmer', None)
        super().__init__(*args, **kwargs)
        if farmer:
            self.fields['farming_area'].queryset = FarmingArea.objects.filter(farmer=farmer)

class UserUpdateForm(forms.ModelForm):
    """Form cập nhật thông tin User"""
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tên'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Họ'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        }
