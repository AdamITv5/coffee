from django.shortcuts import render, get_object_or_404, redirect
from .models import Order
from .forms import OrderForm

# Create your views here.

def order_list(request):
    if request.user.is_staff or request.user.is_superuser:
        orders = Order.objects.all()
    else:
        orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/list.html', {'orders': orders})

def order_edit(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm(instance=order)
    return render(request, 'orders/edit.html', {'form': form})

def order_delete(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        order.delete()
        return redirect('order_list')
    return render(request, 'orders/delete.html', {'order': order})

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from products.models import Product
from .models import Cart, CartItem, OrderItem
from django.db.models import F

@login_required
@require_http_methods(["POST"])
def cart_add(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product,
        defaults={'quantity': 1}
    )
    
    if not created:
        cart_item.quantity = F('quantity') + 1
        cart_item.save()
        cart_item.refresh_from_db()
    
    return JsonResponse({
        'status': 'success',
        'message': 'تمت إضافة المنتج إلى السلة',
        'cart_total': cart.get_total_price()
    })

@login_required
def cart_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'orders/cart.html', {
        'cart': cart,
        'cart_items': cart.items.all()
    })

@login_required
@require_http_methods(["POST"])
def cart_update(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    action = request.POST.get('action')
    
    if action == 'increase':
        cart_item.quantity = F('quantity') + 1
    elif action == 'decrease':
        if cart_item.quantity > 1:
            cart_item.quantity = F('quantity') - 1
        else:
            cart_item.delete()
            return JsonResponse({'message': 'تم حذف المنتج من السلة'})
    
    cart_item.save()
    cart_item.refresh_from_db()
    
    return JsonResponse({
        'message': 'تم تحديث السلة',
        'item_total': cart_item.get_total_price(),
        'cart_total': cart_item.cart.get_total_price()
    })

@login_required
@require_http_methods(["POST"])
def order_create(request):
    cart = get_object_or_404(Cart, user=request.user)
    if not cart.items.exists():
        return JsonResponse({'status': 'error', 'message': 'السلة فارغة'})

    order = Order.objects.create(
        user=request.user,
        status='pending',
        total_price=cart.get_total_price()
    )

    for item in cart.items.all():
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price=item.get_total_price()
        )

    cart.items.all().delete()  # تفريغ السلة بعد تقديم الطلب

    return JsonResponse({'status': 'success', 'message': 'تم تقديم الطلب بنجاح'})
