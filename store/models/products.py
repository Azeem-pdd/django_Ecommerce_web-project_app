from typing import NewType
from django.db import models
from .catagory import Catagory
from datetime import date, datetime, timedelta, timezone
class Products(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=200)
    img = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    date = models.DateTimeField(default=datetime.now,blank=True)
    quantity = models.IntegerField()
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE)
    no_of_visits = models.PositiveIntegerField(default=0)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    

        
    @staticmethod
    def get_all_products():
        return Products.objects.all()
    @staticmethod
    def get_products_by_catagory_id(catagory_id):
        return Products.objects.filter(catagory=catagory_id)
    @staticmethod
    def get_product_by_product_id(cart_products):
        return Products.objects.filter(id__in=cart_products)
    @staticmethod
    def get_product_by_price(price):
        return Products.objects.filter(price__range=(int(price)-48,int(price)+1))
    @staticmethod
    def get_product_by_Recent():
        x=date.today()-timedelta(days=30)
        return Products.objects.filter(date__date__gt=x)
    @staticmethod
    def sort_product_by_Newest():
        return Products.objects.all().order_by('date')
        
    @staticmethod
    def sort_product_by_Popular():
        return Products.objects.all().order_by('-no_of_visits')
    

    @staticmethod
    def get_product_by_prod_id(products):
        x=Products.objects.filter(id=products)
        for a in x:
            b=a.no_of_visits
        Products.objects.filter(id=products).update(no_of_visits=b+1)
        return Products.objects.filter(id=products)