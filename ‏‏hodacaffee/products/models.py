from django.db import models

# Create your models here.

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('drinks', 'مشروبات'),
        ('snacks', 'وجبات خفيفة'),
    ]
    
    name = models.CharField(max_length=255, verbose_name='اسم المنتج')
    description = models.TextField(verbose_name='وصف المنتج')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='السعر')
    stock = models.IntegerField(verbose_name='الكمية المتوفرة')
    category = models.CharField(
        max_length=10,
        choices=CATEGORY_CHOICES,
        default='drinks',
        verbose_name='الفئة'
    )
    image = models.ImageField(upload_to='products/', null=True, blank=True, verbose_name='صورة المنتج')

    class Meta:
        verbose_name = 'منتج'
        verbose_name_plural = 'منتجات'
        ordering = ['category', 'name']

    def __str__(self):
        return self.name
