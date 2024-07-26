from django import template

register = template.Library()

@register.filter(name='multiply')
def multiply(value, arg):
    """
    Multiplies the value by the argument.
    """
    try:
        return value * arg
    except (ValueError, TypeError):
        return ''

@register.filter(name='sum_total')
def sum_total(cart_items):
    """
    Calculates the total price of all items in the cart.
    """
    total = 0
    for item in cart_items:
        total += item.product.price * item.quantity
    return total
