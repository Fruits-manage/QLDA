# Hướng dẫn đăng ký Customer và tạo Stock Movement trong Postman

## 📋 Customer Registration (Đăng ký khách hàng)

### 🎯 Endpoint: Tạo Customer mới
**URL**: `POST http://127.0.0.1:8000/companies/api/create/`

### 📝 Headers:
```
Content-Type: application/json
Accept: application/json
```

### 📋 Request Body (Khách hàng cơ bản):
```json
{
    "name": "Công ty TNHH Thương Mại Trái Cây Việt",
    "company_type": "customer",
    "tax_code": "0987654321",
    "address": "456 Đường Cộng Hòa, Quận Tân Bình, TP.HCM",
    "phone": "028-87654321",
    "email": "info@traicayviet.com",
    "website": "https://traicayviet.com",
    "contact_person": "Trần Thị Lan",
    "contact_phone": "0901234567",
    "contact_email": "lan.tran@traicayviet.com",
    "is_active": true
}
```

### 📋 Request Body (Khách hàng xuất khẩu đầy đủ):
```json
{
    "name": "ABC Export Import Company Ltd",
    "company_type": "customer",
    "tax_code": "1234567890",
    "address": "789 Export Street, District 7, Ho Chi Minh City, Vietnam",
    "phone": "+84-28-12345678",
    "email": "export@abccompany.com",
    "website": "https://abcexport.com",
    "contact_person": "John Smith",
    "contact_phone": "+84-905-123-456",
    "contact_email": "john.smith@abccompany.com",
    "bank_name": "HSBC Bank Vietnam",
    "bank_account": "USD-123456789",
    "import_license": "",
    "export_license": "EXPORT-2024-VN-001",
    "is_active": true
}
```

### ✅ Response thành công:
```json
{
    "success": true,
    "message": "Tạo công ty thành công",
    "data": {
        "id": 5,
        "name": "ABC Export Import Company Ltd",
        "company_type": "customer",
        "tax_code": "1234567890",
        "address": "789 Export Street, District 7, Ho Chi Minh City, Vietnam",
        "phone": "+84-28-12345678",
        "email": "export@abccompany.com",
        "website": "https://abcexport.com",
        "contact_person": "John Smith",
        "contact_phone": "+84-905-123-456",
        "contact_email": "john.smith@abccompany.com",
        "bank_name": "HSBC Bank Vietnam",
        "bank_account": "USD-123456789",
        "import_license": "",
        "export_license": "EXPORT-2024-VN-001",
        "is_active": true,
        "created_at": "2024-08-09T15:30:00.000Z",
        "updated_at": "2024-08-09T15:30:00.000Z"
    }
}
```

### 🔍 Kiểm tra Customer đã tạo:
**URL**: `GET http://127.0.0.1:8000/companies/api/list/?type=customer`

---

## 📦 Stock Movement Creation (Tạo phiếu xuất nhập kho)

### 🎯 Endpoint: Tạo Stock Movement
**URL**: `POST http://127.0.0.1:8000/inventory/movements/api/create/`

### 📝 Headers:
```
Content-Type: application/json
Accept: application/json
```

### 📋 Request Body (Phiếu nhập kho):
```json
{
    "movement_type": "inbound",
    "warehouse_id": 1,
    "reference_number": "IMP-20240809-001",
    "notes": "Nhập kho hàng mới từ nhà cung cấp",
    "expected_date": "2024-08-10",
    "items": [
        {
            "product_id": 1,
            "quantity": 100.0,
            "unit_cost": 25000.0,
            "notes": "Thanh long ruột đỏ, chất lượng cao"
        },
        {
            "product_id": 2,
            "quantity": 50.0,
            "unit_cost": 45000.0,
            "notes": "Xoài cát Hòa Lộc"
        }
    ]
}
```

### 📋 Request Body (Phiếu xuất kho):
```json
{
    "movement_type": "outbound",
    "warehouse_id": 1,
    "reference_number": "EXP-20240809-001",
    "notes": "Xuất kho theo đơn hàng DO-000001",
    "expected_date": "2024-08-09",
    "order_id": 1,
    "items": [
        {
            "product_id": 1,
            "quantity": 20.0,
            "unit_cost": 25000.0,
            "notes": "Xuất cho đơn hàng xuất khẩu"
        },
        {
            "product_id": 2,
            "quantity": 10.0,
            "unit_cost": 45000.0,
            "notes": "Xuất cho đơn hàng xuất khẩu"
        }
    ]
}
```

### 📋 Request Body (Điều chuyển kho):
```json
{
    "movement_type": "transfer",
    "warehouse_id": 1,
    "destination_warehouse_id": 2,
    "reference_number": "TRF-20240809-001",
    "notes": "Điều chuyển hàng từ kho chính đến kho phân phối",
    "expected_date": "2024-08-10",
    "items": [
        {
            "product_id": 1,
            "quantity": 15.0,
            "unit_cost": 25000.0,
            "notes": "Điều chuyển để cân bằng tồn kho"
        }
    ]
}
```

### ✅ Response thành công:
```json
{
    "success": true,
    "message": "Tạo phiếu xuất nhập kho thành công",
    "data": {
        "id": 12,
        "movement_number": "MOV-20240809-012",
        "movement_type": "inbound",
        "movement_type_display": "Nhập kho",
        "warehouse": {
            "id": 1,
            "name": "Kho Lạnh Trái Cây Quận 7",
            "code": "WH-Q7-001"
        },
        "reference_number": "IMP-20240809-001",
        "notes": "Nhập kho hàng mới từ nhà cung cấp",
        "status": "pending",
        "expected_date": "2024-08-10",
        "actual_date": null,
        "total_items": 2,
        "total_value": 4750000.0,
        "created_at": "2024-08-09T15:45:00.000Z",
        "items": [
            {
                "id": 23,
                "product": {
                    "id": 1,
                    "name": "Thanh long ruột đỏ",
                    "code": "TL001"
                },
                "quantity": 100.0,
                "unit_cost": 25000.0,
                "total_cost": 2500000.0,
                "notes": "Thanh long ruột đỏ, chất lượng cao"
            },
            {
                "id": 24,
                "product": {
                    "id": 2,
                    "name": "Xoài cát Hòa Lộc",
                    "code": "XM001"
                },
                "quantity": 50.0,
                "unit_cost": 45000.0,
                "total_cost": 2250000.0,
                "notes": "Xoài cát Hòa Lộc"
            }
        ]
    }
}
```

---

## 🔧 API cho Stock Movement (Cần tạo thêm)

Nếu API chưa có, đây là các endpoint cần tạo:

### 📌 Cần thêm vào `inventory/views.py`:

```python
@method_decorator(csrf_exempt, name='dispatch')
class StockMovementAPICreateView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            
            # Validate required fields
            required_fields = ['movement_type', 'warehouse_id', 'items']
            for field in required_fields:
                if not data.get(field):
                    return JsonResponse({
                        'success': False,
                        'error': f'Trường {field} là bắt buộc'
                    }, status=400)
            
            # Validate movement_type
            valid_types = ['inbound', 'outbound', 'transfer', 'adjustment']
            if data['movement_type'] not in valid_types:
                return JsonResponse({
                    'success': False,
                    'error': f'Loại phiếu không hợp lệ. Chọn từ: {", ".join(valid_types)}'
                }, status=400)
            
            # Check warehouse exists
            try:
                warehouse = Warehouse.objects.get(id=data['warehouse_id'])
            except Warehouse.DoesNotExist:
                return JsonResponse({
                    'success': False,
                    'error': 'Kho không tồn tại'
                }, status=400)
            
            with transaction.atomic():
                # Create movement
                movement = StockMovement.objects.create(
                    movement_type=data['movement_type'],
                    warehouse=warehouse,
                    reference_number=data.get('reference_number', ''),
                    notes=data.get('notes', ''),
                    expected_date=data.get('expected_date'),
                    created_by_id=1  # Replace with request.user.id
                )
                
                # Generate movement number
                movement.movement_number = f"MOV-{movement.created_at.strftime('%Y%m%d')}-{movement.id:03d}"
                movement.save()
                
                # Create movement items
                total_value = 0
                items_data = []
                
                for item_data in data['items']:
                    try:
                        product = Product.objects.get(id=item_data['product_id'])
                        quantity = float(item_data['quantity'])
                        unit_cost = float(item_data.get('unit_cost', 0))
                        total_cost = quantity * unit_cost
                        
                        # Create movement item (you need this model)
                        # movement_item = StockMovementItem.objects.create(...)
                        
                        total_value += total_cost
                        
                        items_data.append({
                            'product': {
                                'id': product.id,
                                'name': product.name,
                                'code': product.code
                            },
                            'quantity': quantity,
                            'unit_cost': unit_cost,
                            'total_cost': total_cost,
                            'notes': item_data.get('notes', '')
                        })
                        
                    except Product.DoesNotExist:
                        return JsonResponse({
                            'success': False,
                            'error': f'Sản phẩm ID {item_data["product_id"]} không tồn tại'
                        }, status=400)
                
                return JsonResponse({
                    'success': True,
                    'message': 'Tạo phiếu xuất nhập kho thành công',
                    'data': {
                        'id': movement.id,
                        'movement_number': movement.movement_number,
                        'movement_type': movement.movement_type,
                        'warehouse': {
                            'id': warehouse.id,
                            'name': warehouse.name,
                            'code': warehouse.code
                        },
                        'reference_number': movement.reference_number,
                        'notes': movement.notes,
                        'status': movement.status,
                        'expected_date': movement.expected_date.isoformat() if movement.expected_date else None,
                        'total_items': len(items_data),
                        'total_value': total_value,
                        'created_at': movement.created_at.isoformat(),
                        'items': items_data
                    }
                })
                
        except json.JSONDecodeError:
            return JsonResponse({
                'success': False,
                'error': 'Dữ liệu JSON không hợp lệ'
            }, status=400)
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': f'Lỗi server: {str(e)}'
            }, status=500)
```

### 📌 Thêm URL vào `inventory/urls.py`:
```python
path('movements/api/create/', views.StockMovementAPICreateView.as_view(), name='movement_api_create'),
```

---

## 🔍 Kiểm tra dữ liệu đã tạo

### Customer:
- **List**: `GET http://127.0.0.1:8000/companies/api/list/`
- **Detail**: `GET http://127.0.0.1:8000/companies/api/{id}/`

### Stock Movement:
- **List**: `GET http://127.0.0.1:8000/inventory/movements/`
- **Detail**: `GET http://127.0.0.1:8000/inventory/movements/{id}/`

---

## ❌ Xử lý lỗi thường gặp

### Customer Creation:
- **Tax code trùng**: Thay đổi `tax_code`
- **Tên công ty trùng**: Thay đổi `name`
- **Email không hợp lệ**: Kiểm tra format email

### Stock Movement:
- **Warehouse không tồn tại**: Kiểm tra `warehouse_id`
- **Product không tồn tại**: Kiểm tra `product_id`
- **Số lượng âm**: Quantity phải > 0
- **Movement type không hợp lệ**: Chỉ chọn từ `inbound`, `outbound`, `transfer`, `adjustment`

---

## 📝 Lưu ý quan trọng

1. **Customer ID**: Lưu lại ID của customer vừa tạo để sử dụng cho orders
2. **Warehouse ID**: Cần có warehouse trước khi tạo stock movement
3. **Product ID**: Cần có products trong hệ thống trước
4. **Reference Number**: Nên unique để dễ theo dõi
5. **Date Format**: Sử dụng YYYY-MM-DD cho dates

**Chúc bạn test API thành công!** 🎉
