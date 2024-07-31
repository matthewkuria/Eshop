from django.shortcuts import render, redirect, HttpResponseRedirect 
from ..models.products import Products 
from ..models.category import Category 
from django.views import View 
from ..forms import SearchForm


class Index(View): 

	def post(self, request): 
		product = request.POST.get('product') 
		remove = request.POST.get('remove') 
		cart = request.session.get('cart') 
		if cart: 
			quantity = cart.get(product) 
			if quantity: 
				if remove: 
					if quantity <= 1: 
						cart.pop(product) 
					else: 
						cart[product] = quantity-1
				else: 
					cart[product] = quantity+1

			else: 
				cart[product] = 1
		else: 
			cart = {} 
			cart[product] = 1

		request.session['cart'] = cart 
		print('cart', request.session['cart']) 
		return redirect('homepage') 

	def get(self, request): 
		# print() 
		return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}') 


def store(request):	
    products = Products.objects.all()
    categories = Category.get_all_categories()	
    context = {'products': products, 'categories': categories }
    return render(request, 'store/index.html', context)

def product_detail(request, product_id):
    product = Products.objects.get(id=product_id)
    context = {'product': product}
    return render(request, 'store/product_detail.html', context)


def search(request):
    form = SearchForm()
    query = None
    results = []
    
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Products.objects.filter(name__icontains=query)  # Adjust the filter as needed

    return render(request, 'store/search_results.html', {'form': form, 'query': query, 'results': results})
