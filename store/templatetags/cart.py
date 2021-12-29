from django import template

from store.models.customer import Customer
from ..models.profile import Profile

register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(product,cart):
    keys = cart.keys()

    for key in keys:
        if int(key) == product.id:
            return True
    return False
@register.filter(name='product_quantity') 
def product_quantity(product,cart):
    if cart:
        keys = cart.keys()
        q=0
        for key in keys:
            if int(key)==product.id:
                q=cart.get(key)
        return q
            
                
            
        
@register.filter(name='prod_quantity') 
def prod_quantity(product):
    return product.quantity
@register.filter(name='prod_price_total')
def prod_price_total(product,cart):
    return product.price*product_quantity(product,cart)

@register.filter(name='cart_price_total')
def cart_price_total(products,cart):
    sum = 0
    try:
        for p in products:
            sum+=prod_price_total(p,cart)
        return sum
    except:
        return sum
@register.filter(name='total_payable')
def total_payable(products,cart):
    return cart_price_total(products, cart)+1
        
@register.filter(name='multiply')
def multiply(number, number1):
    return number*number1
@register.filter(name='check_customer_profile')
def check_customer_profile(customer):
    x=Profile.objects.filter(customer=customer).first()
    if x:
        return True
    else:
        return False
@register.filter(name='product_out_of_stock')
def product_out_of_stock(product,cart):
    keys = cart.keys()

    if product.quantity>cart[str(product.id)]:
        return False
    else:
        return True
@register.filter(name='prod_out_of_stock')
def prod_out_of_stock(product,cart):
    keys = cart.keys()

    if product.quantity>cart[str(product.id)]:
        return False
    else:
        return True