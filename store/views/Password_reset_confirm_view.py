from django.contrib.auth.views import PasswordResetConfirmView
from django.core.exceptions import ValidationError
from ..forms.password_reset_confirm_form import CustPasswordSetForm
from django.shortcuts import redirect, render, HttpResponseRedirect
from .password_reset_view import PasswordResetView
from ..models.customer import Customer

from django.contrib.auth.hashers import make_password

INTERNAL_RESET_SESSION_TOKEN = '_password_reset_token'


class CustPasswordResetConfirmView(PasswordResetConfirmView):
    
    def get(self, request, *args, **kwargs):
        assert 'uidb64' in kwargs and 'token' in kwargs
        
        
        self.uid=self.kwargs['uidb64']
        self.token=self.kwargs['token']
        self.user=Customer.objects.get(id=self.uid)
        
        context={}
        return render(request,'password_reset_confirm.html', context)
    def post(self, request, *args, **kwargs):
            assert 'uidb64' in kwargs
            self.uid=self.kwargs['uidb64']
            password=request.POST.get('new_password1')
            confirm_password=request.POST.get('new_password2')
            
            if type(password)==int or len(password)<8:
                return redirect(self.request.path)
            
            elif password==confirm_password:
                cust=Customer.objects.get(id=self.uid)
                cust.password=make_password(password)
                cust.confirm_password=make_password(confirm_password)
                cust.save()
                return redirect('password_reset_complete')
                
            else:
                return redirect(self.request.path)
    
    def get_user(self, uidb64):
        try:
            # urlsafe_base64_decode() decodes to bytestring
            self.uid=uidb64
            user = Customer.objects.get(id=self.uid)
        except (TypeError, ValueError, OverflowError, Customer.DoesNotExist, ValidationError):
            user = None
        return user