from django.urls import path
from . import views
from . import api

urlpatterns = [
    path('', views.product_list, name='product_list'),
    # روابط خاصة بالمسؤول فقط
    path('add/', views.product_add, name='product_add'),
    path('edit/<int:pk>/', views.product_edit, name='product_edit'),
    path('delete/<int:pk>/', views.product_delete, name='product_delete'),
    path('api/list/', api.api_product_list, name='api_product_list'),
    path('api/add/', api.api_product_add, name='api_product_add'),
    path('api/edit/<int:pk>/', api.api_product_edit, name='api_product_edit'),
    path('api/delete/<int:pk>/', api.api_product_delete, name='api_product_delete'),
]
