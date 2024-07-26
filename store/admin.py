from django.contrib import admin
from .models import Category, Products, Customer, Order, OrderItem, Cart, CartItem

admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Category)
admin.site.register(Products)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
