from django import template
from ..models.products import Products
from ..models.order import Order
from ..models.orderproduct import OrderProduct


register = template.Library()

@register.filter(name='get_object_related_products')
def get_object_related_products(o, cust):
    l = []
    id = o.id
    prods = list(Order.objects.filter(id=id).values('products'))
    for a in range(0,len(prods)):
        l.append(prods[a]['products'])
    prods = Products.objects.filter(id__in=l)  # to be passed as context 
    return prods
@register.filter(name='get_product_quantity')
def get_product_quantity(o,p):
    obj = OrderProduct.objects.filter(order=o,product=p).first()
    q=obj.quantity
    return q
@register.filter(name='get_order_total')
def get_order_total(o,p):
    q=get_product_quantity(o,p)
    return p.price*q
