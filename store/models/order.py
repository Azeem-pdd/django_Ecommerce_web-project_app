
from django.db import models
from django.db.models.enums import Choices
from django.db.models.fields.related import ManyToManyField
from .customer import Customer
from .products import Products
from .payment_method import Payment_method
from datetime import datetime

Order_status_choices = (
    ('created', 'Created'),
    ('approved', 'Approved'),
    ('paid','Paid'),
    ('packaged','Packaged'),
    ('shipped','Shipped'),
    ('completed','Completed'),
)

class Order(models.Model):
    name = models.CharField(max_length=20, default="")
    products = models.ManyToManyField(Products)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    address = models.CharField(max_length=100, default='')
    order_status = models.CharField(max_length=20, choices = Order_status_choices, default='created')
    shipping_address = models.CharField(max_length=100, default='')
    phno = models.BigIntegerField(default=00000000000)
    email = models.EmailField(default="")
    date = models.DateTimeField(default=datetime.now,blank=True)
    price = models.IntegerField(default=0)
    payment_method = models.ForeignKey(Payment_method, on_delete=models.DO_NOTHING, null=True)
    name_additional = models.CharField(max_length=20, null=True,blank=True)
    phno_additional = models.BigIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

    @staticmethod
    def get_order_by_customer_id(customer):
        return Order.objects.filter(customer=customer)
