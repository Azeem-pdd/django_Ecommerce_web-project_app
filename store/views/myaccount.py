from django.utils.decorators import method_decorator
from ..middlewares.authorization import auth_middleware
from store.models.customer import Customer
from django.views import View
from django.shortcuts import render,redirect
from ..models.order import Order
from ..models.profile import Profile
from ..forms.ProfileForm import ProfileForm
class MyAccount(View):
    @method_decorator(auth_middleware)
    def get(self, request):
        customer = request.session.get('customer')
        orders = Order.get_order_by_customer_id(customer)
        

        if customer:
            profile = Profile.whether_customer_exists(customer)
            form = None
            form = ProfileForm(instance=profile)
            context = {
                'form':form,
                'orders':orders
            }
            if profile:
                context['profile'] = profile
            
            
        return render(request, 'my-account.html',context)
    def post(self, request):
        customer = request.session.get('customer')
        if customer:
            profile = Profile.whether_customer_exists(customer)
            if profile:
                form = ProfileForm(request.POST or None, request.FILES or None,instance=profile)
                if form.is_valid():
                    form.save()
                
            else:
                cust = Customer.objects.filter(id = customer).first()
                
                
                
                form = ProfileForm(request.POST or None, request.FILES or None)
                form1 = form.save(commit=False)
                form1.customer = cust
                form1.save()
                
            
            form = ProfileForm(instance=profile)
            context = {'form':form}

            return render(request, 'my-account.html',context)
                

                
            
        else:
            return redirect('login')