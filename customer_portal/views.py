from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.db.models import Q, Count
from management.models import Customer, Farmer
from products.models import Product
from orders.models import Order
from news.models import News

class CustomerHomeView(TemplateView):
    template_name = 'customer_portal/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Get statistics
        context['total_users'] = Customer.objects.filter(is_active=True).count()
        context['total_products'] = Product.objects.filter(is_active=True).count()
        context['total_farmers'] = Farmer.objects.filter(is_active=True).count()
        context['total_orders'] = Order.objects.all().count()
        
        # Get featured products
        try:
            context['featured_products'] = Product.objects.filter(
                is_active=True,
                is_featured=True
            )[:8]
        except:
            context['featured_products'] = []
            
        # Get latest news
        try:
            context['latest_news'] = News.objects.filter(
                is_published=True
            ).order_by('-created_at')[:3]
        except:
            context['latest_news'] = []
            
        return context

class ProductListView(ListView):
    model = Product
    template_name = 'customer_portal/product_list.html'
    context_object_name = 'products'
    paginate_by = 12
    
    def get_queryset(self):
        queryset = Product.objects.filter(is_active=True)
        
        # Search
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(
                Q(name__icontains=search) |
                Q(description__icontains=search)
            )
            
        # Filter by category
        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(category=category)
            
        return queryset.order_by('-created_at')
