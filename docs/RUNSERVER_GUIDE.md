# HƯỚNG DẪN CHẠY HỆ THỐNG 3 PORTAL

## 🚀 **QUICK START GUIDE**

### 1. Admin Portal (Quản trị viên)
```bash
cd "d:\IT\summer-2\QLDA\admin"
python manage.py runserver 8081
```
- **URL**: http://127.0.0.1:8081/
- **Role**: admin
- **Login**: Django Admin authentication

### 2. Customer Portal (Khách hàng)
```bash
cd "d:\IT\summer-2\QLDA\customer"
python manage.py runserver 8080
```
- **URL**: http://127.0.0.1:8080/
- **Role**: customer
- **Login**: Custom authentication

### 3. Farmer Portal (Nông dân)
```bash
cd "d:\IT\summer-2\QLDA\farmer"
python manage.py runserver 8000
```
- **URL**: http://127.0.0.1:8000/
- **Role**: farmer
- **Login**: Shared authentication with customer

---

## 📁 **CẤU TRÚC DỰ ÁN**

```
QLDA/
├── admin/           # Admin Portal (Port 8081)
├── customer/        # Customer Portal (Port 8080)
├── farmer/          # Farmer Portal (Port 8000)
├── shared_templates/ # Shared login/register templates
└── docs/            # Documentation
    ├── ADMIN_FEATURES.md
    ├── CUSTOMER_FEATURES.md
    ├── FARMER_FEATURES.md
    └── RUNSERVER_GUIDE.md
```

---

## 🔑 **ROLE-BASED ACCESS SYSTEM**

### Admin Portal Features
- ✅ **Full system control**: Complete admin functionality
- ✅ **User management**: Manage all users across portals
- ✅ **Data management**: CRUD operations on all models
- ✅ **Reports & Analytics**: System-wide reporting
- ✅ **API endpoints**: Administrative API access

### Customer Portal Features
- ✅ **Product browsing**: View available products
- ✅ **Order management**: Create and track orders
- ✅ **Profile management**: Customer account settings
- ✅ **Payment tracking**: Financial transaction history
- ❌ **No admin access**: Cannot access admin functions

### Farmer Portal Features
- ✅ **Production management**: Farm and crop data
- ✅ **Supply coordination**: Order fulfillment
- ✅ **Quality reporting**: Product quality feedback
- ✅ **Financial tracking**: Revenue and payments
- ❌ **No admin access**: Cannot access admin functions
- ❌ **No customer data**: Cannot access customer info

---

## 🔐 **AUTHENTICATION SYSTEM**

### Shared Authentication
- **Customer & Farmer**: Use shared login/register templates
- **Location**: `shared_templates/auth/`
- **Auto-detection**: Templates detect portal type automatically

### Separate User Models
- **Admin**: `admin/accounts/models.py` - Role='admin'
- **Customer**: `customer/accounts/models.py` - Role='customer'
- **Farmer**: `farmer/accounts/models.py` - Role='farmer'

---

## 🛠️ **DEVELOPMENT SETUP**

### Prerequisites
- Python 3.12+
- Django 4.2.7
- MySQL Database
- Git

### Installation Steps
1. **Clone repository**
   ```bash
   git clone <repository-url>
   cd QLDA
   ```

2. **Setup Virtual Environment** (for each portal)
   ```bash
   cd admin
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Database Configuration**
   - Update `settings.py` in each portal
   - Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create Superuser** (Admin portal only)
   ```bash
   cd admin
   python manage.py createsuperuser
   ```

---

## 🔄 **DATA SYNCHRONIZATION**

### Inter-Portal Communication
- **API Integration**: REST APIs for data sharing
- **Real-time Updates**: Cross-portal data synchronization
- **Shared Database**: Some models shared across portals

### Data Flow
```
Admin Portal (Master)
    ↓ Orders, Products, Pricing
Customer Portal ← → Farmer Portal
    ↑ Customer Data     ↑ Supply Data
```

---

## 📊 **MONITORING & LOGS**

### System Health Checks
- **Admin**: http://127.0.0.1:8081/admin/
- **Customer**: http://127.0.0.1:8080/dashboard/
- **Farmer**: http://127.0.0.1:8000/dashboard/

### Log Files
- Check Django console output for errors
- Monitor database connections
- Track API response times

---

## 🚀 **PRODUCTION DEPLOYMENT**

### Environment Variables
```bash
# Database
DB_NAME=fruit_export_db
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=3306

# Security
SECRET_KEY=your_secret_key
DEBUG=False
ALLOWED_HOSTS=your_domain.com

# Static Files
STATIC_ROOT=/var/www/static/
MEDIA_ROOT=/var/www/media/
```

### Nginx Configuration
```nginx
# Admin Portal
server {
    listen 80;
    server_name admin.yoursite.com;
    location / {
        proxy_pass http://127.0.0.1:8081;
    }
}

# Customer Portal
server {
    listen 80;
    server_name customers.yoursite.com;
    location / {
        proxy_pass http://127.0.0.1:8080;
    }
}

# Farmer Portal
server {
    listen 80;
    server_name farmers.yoursite.com;
    location / {
        proxy_pass http://127.0.0.1:8000;
    }
}
```

---

## 🔧 **TROUBLESHOOTING**

### Common Issues

#### Port Already in Use
```bash
# Check what's using the port
netstat -ano | findstr :8080
# Kill the process
taskkill /PID <PID> /F
```

#### Database Connection Error
- Verify MySQL is running
- Check database credentials in settings.py
- Ensure database exists

#### Module Import Errors
- Activate virtual environment
- Install missing packages: `pip install -r requirements.txt`
- Check Python path

#### Template Not Found
- Verify template paths in settings.py
- Check if shared_templates directory exists
- Ensure template files are in correct locations

---

## 📈 **PERFORMANCE OPTIMIZATION**

### Production Settings
- **DEBUG = False**: Disable debug mode
- **ALLOWED_HOSTS**: Set proper allowed hosts
- **Static files**: Configure static file serving
- **Database**: Optimize database queries
- **Caching**: Implement Redis/Memcached

### Monitoring
- **APM Tools**: New Relic, Datadog
- **Log Analysis**: ELK Stack
- **Database Monitoring**: MySQL performance schema
- **Health Checks**: Automated monitoring

---

## 🔒 **SECURITY CHECKLIST**

### Production Security
- ✅ **HTTPS**: SSL certificate installed
- ✅ **CSRF Protection**: Django CSRF middleware
- ✅ **XSS Protection**: Template auto-escaping
- ✅ **SQL Injection**: Use Django ORM
- ✅ **Secure Headers**: Security middleware
- ✅ **Rate Limiting**: API rate limiting
- ✅ **Input Validation**: Proper form validation

---

## 📝 **MAINTENANCE**

### Regular Tasks
- **Database Backup**: Daily automated backups
- **Log Rotation**: Automatic log file rotation
- **Security Updates**: Keep Django and dependencies updated
- **Performance Monitoring**: Regular performance reviews

### Updates & Migrations
```bash
# Update code
git pull origin main

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic

# Restart services
sudo systemctl restart gunicorn
sudo systemctl restart nginx
```

---

## 📞 **SUPPORT**

### Getting Help
- **Documentation**: Check feature documentation files
- **Logs**: Review Django console output
- **Database**: Check MySQL logs
- **Community**: Django community forums

### Development Team
- **Backend**: Django developers
- **Frontend**: Bootstrap/jQuery developers
- **DevOps**: System administrators
- **Database**: MySQL administrators

---

*Tài liệu này được cập nhật thường xuyên. Vui lòng kiểm tra phiên bản mới nhất.*

*Cập nhật: August 22, 2025*
*Version: 1.0*
