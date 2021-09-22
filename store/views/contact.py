from django.views import View
from django.shortcuts import render,redirect

class Contact(View):
    def get(self, request):
        return render(request,'contact.html')