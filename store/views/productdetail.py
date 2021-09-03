from django.views import View
from django.shortcuts import render,redirect
from ..models.products import Products
class ProductDetail(View):
    def get(self, request):
        info = request.GET.get('info')
        product = request.GET.get('product')
        prods = {}
        prods['products'] = Products.get_all_products()
        cart = request.session.get('cart')
        if not cart:
            request.session.cart = {}
        if info:
            prods['prod'] = Products.get_product_by_prod_id(product)
        else:
            pass
        return render(request,'product-detail.html',prods)


    def post(self,request):

        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        quantity = cart.get(product)
        if cart:
            if remove:
                if quantity<=1:
                    cart.pop(product)
                else:
                    cart[product] = quantity  - 1
            

            else:
                
                cart[product] = quantity + 1
            

        else:
            request.session.cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        return redirect('product-detail')