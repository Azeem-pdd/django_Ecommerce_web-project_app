from store.views.wishlist import Wishlist
from django.views import View
from django.shortcuts import render,redirect
from ..models.products import Products
from ..templatetags import cart as c
class Cart(View):
    def get(self, request):
        cart = request.session.get('cart')
        products = None
        if not cart:
            request.session.cart = {}
        else:
            cart_products = list(cart.keys())
            
            products= Products.get_product_by_product_id(cart_products)
        return render(request,'cart.html',{'products':products})
    
    def post(self,request):

        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        delete = request.POST.get('delete')
        quantity = cart.get(product)
        if cart:
            if remove:
                if quantity<=1:
                    cart.pop(product)
                else:
                    cart[product] = quantity  - 1
            elif delete:
                cart.pop(product)

            else:
                if c.prod_out_of_stock(Products.objects.get(id=product), cart):
                    pass
                else:
                    cart[product] = quantity + 1
            

        else:
            request.session.cart = {}

        request.session['cart'] = cart
        return redirect('cart')