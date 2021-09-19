from django.shortcuts import get_object_or_404
from django.http.response import HttpResponse
from store.models.orderproduct import OrderProduct
from django.views import View
from django.shortcuts import render,redirect
from django.utils.decorators import method_decorator
from ..middlewares.authorization import auth_middleware
from ..models.profile import Profile
from ..models.products import Products
from ..models.customer import Customer
from ..models.payment_method import Payment_method
from ..models.order import Order
from ..templatetags import cart as c
class Checkout(View):
    @method_decorator(auth_middleware)
    def get(self, request):
        customer = request.session.get('customer')
        cust = Customer.objects.filter(id=customer).first
        cart = request.session.get('cart')
        ids = []
        products = None
        if cart:

            ids = list(cart.keys())
            products = Products.get_product_by_product_id(ids)
            
        if not cart:
            request.session.cart = {}

        
        context = {}
        
        context['products'] = products
        context['customer'] = cust
        context['pay_method'] = Payment_method.get_all_payemnt_methods()
        if customer:
            profile = Profile.whether_customer_exists(customer)
            if profile:
                context['profile'] = profile

        return render(request,'checkout.html', context)

        
    
    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phno = request.POST.get('phno')
        address = request.POST.get('address')
        city = request.POST.get('city')
        zipcode = request.POST.get('zipcode')
        pay_method = request.POST.get('pay_method')
        ship_to_diff_addr = request.POST.get('ship_to_diff_addr')
        name1 = request.POST.get('name1')
        phno1 = request.POST.get('phno1')
        address1 = request.POST.get('address1')
        total_price = request.POST.get('total_price')
        cart = request.session.get('cart')
        keys = None
        products = None
        error_msg=None
        if cart:
            keys = cart.keys()
            products = Products.get_product_by_product_id(keys)
            

        customer = request.session.get('customer')

        cust = Customer.objects.filter(id = customer).first()
        if products!=None:

            if pay_method:
        
                order = Order.objects.create(name = name,
                customer = cust,
                address = address,
                
                phno = phno,
                email = email,
                price = total_price,
                payment_method = Payment_method.objects.filter(id = pay_method).first(),
                


                )
                order.products.set(products)
                if ship_to_diff_addr:
                    order.name_additional = name1
                    order.shipping_address = address1
                    order.phno_additional = phno1
                else:
                    try:
                        order.shipping_address = Profile.objects.get(customer=cust).shipping_address
                    except:
                        pass
                order.save()
                    
            
                    
                for p in products:
                    orderprod = OrderProduct(order = order,
                    product = p,
                    quantity = c.product_quantity(p, cart))
                    orderprod.save()
                request.session['cart'] = None
                return redirect('success')
            else:
                error_msg='Choose payment method'
        else:
            error_msg='No Products in cart. Enter Products in Cart First.'
        if error_msg:
            return render(request, 'checkout.html', {'error_msg':error_msg})