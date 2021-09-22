from django.views import View
from django.shortcuts import render,redirect
from .index import Index

class ProductView(View):
    def get(self, request):
       
        return render(request,'product-list.html',Index.dict(request))
    def post(self,request):
        
        product = request.POST.get('product')
        add_to_cart = request.POST.get('add_to_cart')
        add_to_wishlist = request.POST.get('add_to_wishlist')
        cart = request.session.get('cart')
        wishlist = request.session.get('wishlist')
        
        
        
        
        try:
            quantity = cart[product]
            items = wishlist[product]
        except:
            quantity = None
            items = None
        

        if add_to_cart:        
            if cart:
                if quantity:
                    cart[product] = quantity+1
                else:
                    cart[product] = 1
            else:
                cart = {}
                cart[product] = 1
            request.session['cart'] = cart
            
        
        elif add_to_wishlist:
            if wishlist:
                if items:
                    wishlist[product] = items+1
                else:
                    wishlist[product] = 1
            else:
                wishlist = {}
                wishlist[product] = 1
            request.session['wishlist'] = wishlist
        
        return redirect('product-list')