from django.utils.decorators import method_decorator
from ..middlewares.authorization import auth_middleware
from store.models.customer import Customer
from django.views import View
from django.shortcuts import render,redirect
from ..models.order import Order
from ..models.orderproduct import OrderProduct
from ..models.profile import Profile
from ..forms.ProfileForm import ProfileForm
from ..models.payment_method import Payment_method
class MyAccount(View):
    @method_decorator(auth_middleware)
    def get(self, request):
        customer = request.session.get('customer')
        

        if customer:
            profile = Profile.fetch_customer_profile(customer)
            form = None
            context=OrderProduct.fetch_customer_order_objects(customer)
            
            
            
            if profile:

                form = None
                form = ProfileForm(instance=profile)
                context['form']=form
                context['profile'] = profile
                payment_method = Payment_method.objects.all()
                context['payment_method'] = payment_method
            else:
                form=ProfileForm()
                context['form']=form

        return render(request, 'my-account.html',context)

    def post(self, request):
        customer = request.session.get('customer')
        if customer:
            profile = Profile.fetch_customer_profile(customer)
            if profile:
                form = ProfileForm(request.POST or None, request.FILES or None,instance=profile)
                if form.is_valid():
                    form.save()
                
            else:
                cust = Customer.objects.filter(id = customer).first()
                
                form = ProfileForm(request.POST or None, request.FILES or None)
                if form.is_valid():
                    form1 = form.save(commit=False)
                    form1.customer = cust
                    form1.save()
                
            
            form = ProfileForm(instance=profile)
            context = {'form':form}

            return redirect('myaccount')
                

                
            
        else:
            return redirect('login')