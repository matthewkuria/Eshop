from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from ..forms import CheckoutForm
from django.contrib import messages
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

@login_required
def checkout(request):
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # Process payment (this is just a placeholder, integrate with a real payment gateway)
            payment_method = form.cleaned_data.get('payment_method')
            if payment_method == 'card':
                card_number = form.cleaned_data.get('card_number')
                expiry_date = form.cleaned_data.get('expiry_date')
                cvv = form.cleaned_data.get('cvv')
                # Process card payment (add your payment gateway integration here)
            elif payment_method == 'paypal':
                # Process PayPal payment (add your PayPal integration here)
                pass

            # Create order
            order.address = form.cleaned_data.get('address')
            order.city = form.cleaned_data.get('city')
            order.state = form.cleaned_data.get('state')
            order.zip_code = form.cleaned_data.get('zip_code')
            order.complete = True
            order.save()

            # Clear cart
            items.delete()

            messages.success(request, 'Your order has been placed successfully!')
            return redirect('order_confirmation')
    else:
        form = CheckoutForm()

    context = {
        'items': items,
        'order': order,
        'form': form,
    }
    return render(request, 'store/checkout.html', context)
    
@login_required
def order_confirmation(request):
    return render(request, 'order_confirmation.html')