from django.views import View
from django.shortcuts import render,redirect,HttpResponseRedirect
from ..models.customer import Customer
from django.contrib.auth.hashers import check_password
class Login(View):
    return_url = None
    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        return render(request,'login.html')
    def post(self,request):

        obj = None
        pswd = None
        error_msg = None
        Email = request.POST.get('Email')
        Password = request.POST.get('Password')
        obj = Customer.is_email_valid(Email)
        print(obj)

        if obj==False:
            error_msg = "Invalid Email or password"
        elif check_password(Password,obj.password):
            obj.save()
            request.session['customer'] = obj.id
        else:
            error_msg = "Invalid Email or password"
            
        if not error_msg:
            if Login.return_url:
                return HttpResponseRedirect(Login.return_url)
            else:
                return redirect('index')
        else:
            return render(request,'login.html',{'error_msg':error_msg})
        
