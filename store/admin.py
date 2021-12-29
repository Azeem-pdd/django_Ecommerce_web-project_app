from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin import register
from .models.customer import Customer
from .models.order import Order
from .models.catagory import Catagory
from .models.products import Products
from .models.profile import Profile
from .models.order import Order
from .models.payment_method import Payment_method
from .models.orderproduct import OrderProduct




# Register your models here.
admin.site.register(Catagory)
admin.site.register(Customer)
admin.site.register(Products)
admin.site.register(Order)
admin.site.register(Profile)
admin.site.register(Payment_method)
admin.site.register(OrderProduct)

