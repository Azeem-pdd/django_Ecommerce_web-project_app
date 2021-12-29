from django.contrib.auth import tokens, views as auth_views
from django.contrib.auth import forms as auth_forms

from django.urls import path
from . import views
from .views.index import Index
from .views.cart import Cart
from .views.checkout import Checkout
from .views.contact import Contact
from .views.login import Login
from .views.logout import Logout
from .views.regsiter import Register
from .views.myaccount import MyAccount
from .views.productlist import ProductView
from .views.productdetail import ProductDetail
from .views.wishlist import Wishlist
from .views.search import Search
from .views.success import SuccessView
from .views.password_reset_view import CustPasswordResetView
from .views.Password_reset_confirm_view import CustPasswordResetConfirmView
from .views.paypal import process_payment, payment_done, payment_cancelled
token=tokens
print(token)
urlpatterns = [
    path('',Index.as_view(), name = 'index'),
    path('contact',Contact.as_view(), name = 'contact'),
    path('cart',Cart.as_view(), name = 'cart'),
    path('checkout',Checkout.as_view(), name = 'checkout'),
    path('product-detail',ProductDetail.as_view(), name = 'product-detail'),
    path('product-list',ProductView.as_view(), name = 'product-list'),
    path('login',Login.as_view(), name = 'login'),
    path('logout',Logout.as_view(), name = 'logout'),
    path('register',Register.as_view(), name = 'register'),
    path('my-account',MyAccount.as_view(), name = 'myaccount'),
    path('wishlist',Wishlist.as_view(), name = 'wishlist'),
    path('search',Search.as_view(), name = 'search'),
    path('password_reset', CustPasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>', CustPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('success', SuccessView.as_view(), name='success'),
    path('process_payment', process_payment, name='process_payment'),
    path('payment_done', payment_done, name='payment_done'),
    path('payment_cancelled', payment_cancelled, name='payment_cancelled'),


    
]