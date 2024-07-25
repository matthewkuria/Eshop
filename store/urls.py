from django.contrib import admin 
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path 
from .views.home import Index, store 
from .views.signup import Signup 
from .views.login import Login, logout 
from .views.cart import Cart 
from .views.checkout import CheckOut 
from .views.orders import OrderView 
from users import views as user_views
from django.contrib.auth import views as auth_views

# from .middlewares.auth import auth_middleware 


urlpatterns = [ 
	path('', Index.as_view(), name='homepage'), 
	path('store', store, name='store'), 
	path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('password-reset/done', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
	 
	path('cart', Cart, name='cart'), 
	path('check-out', CheckOut.as_view(), name='checkout'), 
	path('orders', OrderView.as_view(), name='orders'), 

] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
