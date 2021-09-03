from django.shortcuts import get_object_or_404
from django.db.models import Case, When
from django.db import models
from django.db.models.fields.related import ForeignKey
from .order import Order
from .products import Products
class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product.name

    @staticmethod
    def sort_product_by_Most_sale():
        list1=list(Products.objects.all())
        dic = {}
        dict = {}
        
        for l in list1:
            objs = OrderProduct.objects.filter(product = l)
            dic[l.id] = 0
            for o in objs:
                dic[l.id] += o.quantity
        
        n = len(dic.values())
        try:
            for v in range(1,n+1):
                keys = dic.keys()
                g = 2
                for k in keys:
                
                    if dic[k]>dic[g]:
                        g=k
                
                dict[g] = dic[g]
                dic.pop(g)
                        
                        
        except:
            pass
        dict.update(dic)
        p_list = list(dict.keys())
        
        
        preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(p_list)])
        queryset = Products.objects.filter(pk__in=p_list).order_by(preserved)
        return queryset

    @staticmethod
    def get_product_by_Most_sale():
        list1=list(Products.objects.all())
        dic = {}
        dict = {}
        
        for l in list1:
            objs = OrderProduct.objects.filter(product = l)
            dic[l.id] = 0
            for o in objs:
                dic[l.id] += o.quantity
        
        n = len(dic.values())
        try:
            for v in range(1,n+1):
                keys = dic.keys()
                g = 2
                for k in keys:
                
                    if dic[k]>dic[g]:
                        g=k
                
                dict[g] = dic[g]
                dic.pop(g)
                        
                        
        except:
            pass
        dict.update(dic)
        p_list = list(dict.keys())
        
        
        preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(p_list)])
        queryset = Products.objects.filter(pk__in=p_list).order_by(preserved)[:5]
        return queryset