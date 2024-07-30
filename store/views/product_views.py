from django.shortcuts import render, get_object_or_404
from ..models.products import Products

def product_list(request):
    products = Products.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    return render(request, 'store/product_detail.html', {'product': product})
