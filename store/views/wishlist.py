from django.views import View
from django.shortcuts import render,redirect
from ..models.products import Products

class Wishlist(View):
    def get(self, request):
        wishlist = request.session.get('wishlist')
        cart = request.session.get('cart')
        products = None
        if not cart:
            request.session.cart = {}
        if not wishlist:
            request.session.wishlist = {}
        

        else:
            cart_products = list(wishlist.keys())
            
            products= Products.get_product_by_product_id(cart_products)
        return render(request,'wishlist.html',{'products':products})

    def post(self,request):

        product = request.POST.get('product')
        delete = request.POST.get('delete')
        add_to_cart = request.POST.get('add_to_cart')
        wishlist = request.session.get('wishlist')
        cart = request.session.get('cart')
        quan = None
        try:
            quantity = cart.get(product)
            quan = wishlist.get(product)
        except:
            pass
        if add_to_cart:
            if cart:
                if quantity:

                    cart[product] = quantity + 1
                else:
                    cart[product] = 1
            else:
                request.session.cart = {}
                cart[product] = 1
            request.session['cart'] = cart
        elif wishlist:
           
            if delete:
                wishlist.pop(product)
                    
        else:
            request.session.wishlist = {}
            wishlist[product] = 1

        request.session['wishlist'] = wishlist

        return redirect('wishlist')