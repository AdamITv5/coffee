from django.urls import path
from . import views
from . import api

urlpatterns = [
    path('orders/', views.order_list, name='order_list'),
    path('orders/edit/<int:order_id>/', views.order_edit, name='order_edit'),
    path('orders/delete/<int:order_id>/', views.order_delete, name='order_delete'),
    path('cart/', views.cart_view, name='cart_view'),
    path('cart/add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('cart/update/<int:item_id>/', views.cart_update, name='cart_update'),
    path('order/create/', views.order_create, name='order_create'),  # مسار جديد لتقديم الطلب
    path('api/orders/', api.api_order_list, name='api_order_list'),
    path('api/orders/edit/<int:order_id>/', api.api_order_edit, name='api_order_edit'),
    path('api/orders/delete/<int:order_id>/', api.api_order_delete, name='api_order_delete'),
    path('api/cart/add/<int:product_id>/', api.api_cart_add, name='api_cart_add'),
]
