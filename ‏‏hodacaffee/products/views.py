from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied
from .models import Product

# Create your views here.

def is_admin(user):
    return user.is_superuser

@login_required  # المستخدم العادي يمكنه فقط عرض المنتجات
def product_list(request):
    products = Product.objects.all().order_by('category', 'name')
    return render(request, 'products/list.html', {'products': products})

@user_passes_test(is_admin)  # فقط المسؤول يمكنه إضافة منتجات
def product_add(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    # هذه الدالة للمسؤول فقط
    pass

@user_passes_test(is_admin)  # فقط المسؤول يمكنه تعديل المنتجات
def product_edit(request, pk):
    if not request.user.is_superuser:
        raise PermissionDenied
    # هذه الدالة للمسؤول فقط
    pass

@user_passes_test(is_admin)  # فقط المسؤول يمكنه حذف المنتجات
def product_delete(request, pk):
    if not request.user.is_superuser:
        raise PermissionDenied
    # هذه الدالة للمسؤول فقط
    pass
