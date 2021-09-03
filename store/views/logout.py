from django.views import View
from django.shortcuts import redirect 
from django.contrib.auth.decorators import login_required
from django.contrib import auth
class Logout(View):    
    
    def get(self,request):
        auth.logout(request)
        return redirect('login')