from django.views import View
from django.shortcuts import render,redirect,HttpResponse
from ..models.customer import Customer
from django.contrib.auth.hashers import make_password

class Register(View):
    def get(self, request):
        return render(request,'register.html')
    def post(self,request):


        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        Email = request.POST.get('Email')
        phno = request.POST.get('phno')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')


        customer = Customer(
            first_name=first_name,
            last_name=last_name,
            email=Email,
            phno=phno,
            password=password,
            confirm_password = confirm_password
        )
        values = {'first_name':first_name,
        'last_name':last_name,
        'Email' : Email,
        'phno':phno,
        }


        err_msg = None
        

        
        
        
        
        if customer.password!=customer.confirm_password:
            err_msg = "passwords not matching"
        elif Customer.phno_exists(customer.phno)==True:
            err_msg = "phone number already found!!! enter other"
        elif len(customer.phno)<11:
            err_msg = "phone number must be 11 characters long"
        elif Customer.email_exists(customer.email)==True:
            err_msg = "Email already Exists"
        elif len(customer.last_name)<3:
            err_msg = "last_name must be at least 3 characters long"
        elif len(customer.first_name) < 3:
            err_msg = "first_name must be at least 3 characters long"
        error_msg = err_msg
        
         
        if not error_msg:
            customer.password = make_password(customer.password, salt=None, hasher='default')
            customer.confirm_password = make_password(customer.confirm_password, salt=None, hasher='default')
            customer.save()
            
            return redirect('login')

        else:
            print(error_msg)
            return render(request, 'register.html',{'error_msg':error_msg,'values':values})




        

