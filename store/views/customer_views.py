from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..models.customer import Customer

@login_required
def customer_profile(request):
    customer = Customer.objects.get(user=request.user)
    return render(request, 'store/customer_profile.html', {'customer': customer})
