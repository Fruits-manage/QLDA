from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User  # Import custom User model
from customer_portal.models import CustomerProfile  # Dùng CustomerProfile thay cho management.Customer

class CustomerRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=15, required=True)
    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), required=True)
    
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.role = 'customer'  # Mặc định là khách hàng thường
        
        if commit:
            user.save()
            # Tạo CustomerProfile cho user
            CustomerProfile.objects.create(
                user=user,
                phone=self.cleaned_data["phone"],
                address=self.cleaned_data["address"],
                customer_code=f"CUST{user.id:06d}"  # Tạo mã khách hàng
            )
        return user
