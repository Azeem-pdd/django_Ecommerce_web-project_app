from store.models.profile import Profile
from typing import get_args
from store.views.wishlist import Wishlist
from django.views import View
from django.shortcuts import render,redirect
from ..models.catagory import Catagory
from ..models.products import Products
from ..models.orderproduct import OrderProduct
from datetime import datetime
import calendar
class Index(View):
    
    def dict(request, query="", price=0):
        catagory_id = request.GET.get('catagory')
        sortby = request.GET.get('sortby')
        
        products = None
        recent = Products.get_product_by_Recent()
        featured = Products.objects.filter(featured = True)
        if catagory_id:
            products = Products.get_products_by_catagory_id(catagory_id)
            print(catagory_id)
        elif query:
            products = Products.objects.filter(name__icontains=query)
        elif price:
            products = Products.get_product_by_price(price)
        
        elif sortby:
            
            if sortby=="recent":
                
                products = Products.get_product_by_Recent()
            elif sortby=="newest":
                
                products = Products.sort_product_by_Newest()
            elif sortby=="popular":
                
                products = Products.sort_product_by_Popular()
            elif sortby=="mostsale":
                
                products = OrderProduct.sort_product_by_Most_sale()
            elif sortby=="mostsold":
                
                products = OrderProduct.get_product_by_Most_sale()
            elif sortby=="featured":
                
                products = Products.objects.filter(featured = True)
                
                
        else:
            products = Products.get_all_products()
        customer = request.session.get('customer')
        customer_logged_in = Profile.objects.filter(customer = customer)
        dic = {
            'products':products,
        'recent':recent,
        'featured':featured,
        'customer':customer_logged_in}
        
        
        dic['catagories'] = Catagory.get_all_catagories()
        return dic

    def get(self, request):
        
        cart = request.session.get('cart')
        wishlist = request.session.get('wishlist')
        if not cart:
            cart = {}
        if not wishlist:
            wishlist = {}

        return render(request,'index.html', Index.dict(request))

    def post(self,request):
        
        product = request.POST.get('product')
        add_to_cart = request.POST.get('add_to_cart')
        add_to_wishlist = request.POST.get('add_to_wishlist')
        search = request.POST.get('search')
        cart = request.session.get('cart')
        wishlist = request.session.get('wishlist')
        print(search)
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
        
        return redirect('index')










        