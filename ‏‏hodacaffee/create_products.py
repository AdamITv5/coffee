import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'user_coffee.settings')
django.setup()

from products.models import Product

# قائمة المنتجات
products = [
    {
        'name': 'قهوة عربية',
        'description': 'قهوة عربية أصيلة محضرة على الطريقة التقليدية',
        'price': 15.00,
        'stock': 100,
        'category': 'drinks'
    },
    {
        'name': 'كابتشينو',
        'description': 'قهوة إيطالية مع رغوة الحليب',
        'price': 18.00,
        'stock': 100,
        'category': 'drinks'
    },
    {
        'name': 'لاتيه',
        'description': 'قهوة مع حليب ساخن',
        'price': 16.00,
        'stock': 100,
        'category': 'drinks'
    },
    {
        'name': 'كيكة الشوكولاتة',
        'description': 'كيكة طازجة بالشوكولاتة الداكنة',
        'price': 25.00,
        'stock': 50,
        'category': 'snacks'
    },
    {
        'name': 'كرواسون',
        'description': 'كرواسون فرنسي طازج',
        'price': 12.00,
        'stock': 50,
        'category': 'snacks'
    },
    {
        'name': 'مافن التوت',
        'description': 'مافن محشو بالتوت الطازج',
        'price': 14.00,
        'stock': 50,
        'category': 'snacks'
    }
]

# إضافة المنتجات إلى قاعدة البيانات
for product_data in products:
    # تحقق مما إذا كان المنتج موجود بالفعل
    if not Product.objects.filter(name=product_data['name']).exists():
        Product.objects.create(**product_data)
        print(f"تم إضافة {product_data['name']}")
