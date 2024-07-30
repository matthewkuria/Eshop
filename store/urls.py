from django.contrib import admin 
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path 
from .views.home import Index, store, product_detail
from .views.product_views import product_list
from .views.customer_views import customer_profile
from .views.login import Login, logout 
from .views.order_views import cart_detail, add_to_cart, subtract_from_cart, order_detail, remove_from_cart
from .views.checkout import CheckOut 
from users import views as user_views
from django.contrib.auth import views as auth_views


urlpatterns = [ 
	path('', Index.as_view(), name='homepage'), 
	path('store', store, name='store'), 
    path('product/<int:product_id>/', product_detail, name='product_detail'),    
	path('check-out', CheckOut.as_view(), name='checkout'), 

    # 
    path('products/', product_list, name='product_list'),
    path('products/<int:product_id>/', product_detail, name='product_detail'),
    path('profile/', customer_profile, name='customer_profile'),
    path('cart/', cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/subtract/<int:product_id>/', subtract_from_cart, name='subtract_from_cart'),
    path('cart/remove/<int:product_id>/', remove_from_cart, name='remove_from_cart'),

    # Registration urls
	path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('password-reset/done', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
	

] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
