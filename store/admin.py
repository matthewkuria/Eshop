from django.contrib import admin
from .models import Category, Products, Customer, Order, OrderItem

admin.site.register(Category)
admin.site.register(Products)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
