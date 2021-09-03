from django.views import View
from django.shortcuts import render,redirect

class SuccessView(View):
    def get(self, request):
        return render(request,'success.html')