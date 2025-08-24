from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import CustomerProfile, CustomerAddress, CustomerReview

User = get_user_model()

class CustomerRegistrationForm(UserCreationForm):
    """Form đăng ký khách hàng"""
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
    customer_type = forms.ChoiceField(
        choices=CustomerProfile.CUSTOMER_TYPE_CHOICES,
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

class CustomerProfileForm(forms.ModelForm):
    """Form cập nhật thông tin khách hàng"""
    class Meta:
        model = CustomerProfile
        fields = [
            'customer_type', 'phone', 'province', 'district', 'ward', 'address',
            'company_name', 'tax_code', 'preferred_products', 'preferred_payment_method'
        ]
        widgets = {
            'customer_type': forms.Select(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Số điện thoại'}),
            'province': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tỉnh/Thành phố'}),
            'district': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Quận/Huyện'}),
            'ward': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phường/Xã'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Địa chỉ chi tiết'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tên công ty (nếu có)'}),
            'tax_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mã số thuế (nếu có)'}),
            'preferred_products': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Mô tả sản phẩm bạn thường mua'}),
            'preferred_payment_method': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phương thức thanh toán ưa thích'}),
        }

class CustomerAddressForm(forms.ModelForm):
    """Form thêm/sửa địa chỉ giao hàng"""
    class Meta:
        model = CustomerAddress
        fields = [
            'label', 'recipient_name', 'phone', 'province', 'district', 
            'ward', 'address', 'is_default'
        ]
        widgets = {
            'label': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'VD: Nhà riêng, Công ty'}),
            'recipient_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tên người nhận'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Số điện thoại người nhận'}),
            'province': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tỉnh/Thành phố'}),
            'district': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Quận/Huyện'}),
            'ward': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phường/Xã'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Địa chỉ chi tiết'}),
            'is_default': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class CustomerReviewForm(forms.ModelForm):
    """Form đánh giá sản phẩm"""
    class Meta:
        model = CustomerReview
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.Select(
                choices=[(i, f'{i} sao') for i in range(1, 6)],
                attrs={'class': 'form-control'}
            ),
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Chia sẻ cảm nhận của bạn về sản phẩm này...'
            }),
        }

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
