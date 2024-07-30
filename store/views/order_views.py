from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from ..models.orders import Order, OrderItem
from ..models.products import Products
from ..models.customer import Customer

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Products, id=product_id)    
    try:
        customer = request.user.customer  # Access the related Customer instance
    except Customer.DoesNotExist:
        # Handle the case where the Customer instance does not exist
        # You can redirect the user to a profile creation page or create a Customer instance
        customer = Customer.objects.create(user=request.user, name=request.user.username, email=request.user.email)
    
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    order_item, created = OrderItem.objects.get_or_create(order=order, product=product)
    if not created:
        order_item.quantity += 1
    order_item.save()
    return redirect('cart_detail')

@login_required
def order_detail(request):
    order = get_object_or_404(Order, customer=request.user.customer, complete=False)
    order_items = OrderItem.objects.filter(order=order)
    return render(request, 'store/order_detail.html', {'order': order, 'order_items': order_items})

@login_required
def remove_from_cart(request, order_item_id):
    order_item = get_object_or_404(OrderItem, id=order_item_id)
    order_item.delete()
    return redirect('cart_detail')

@login_required
def subtract_from_cart(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    customer = request.user.customer
    order = get_object_or_404(Order, customer=customer, complete=False)
    order_item = get_object_or_404(OrderItem, order=order, product=product)
    if order_item.quantity > 1:
        order_item.quantity -= 1
        order_item.save()
    else:
        order_item.delete()
    return redirect('cart_detail')

@login_required
def remove_from_cart(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    customer = request.user.customer
    order = get_object_or_404(Order, customer=customer, complete=False)
    order_item = get_object_or_404(OrderItem, order=order, product=product)
    order_item.delete()
    return redirect('cart_detail')

@login_required
def cart_detail(request):
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    context = {'items': items, 'order': order}
    return render(request, 'store/cart_detail.html', context)
