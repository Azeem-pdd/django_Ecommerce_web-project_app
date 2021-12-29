from django.contrib.auth.views import PasswordResetCompleteView

from django.shortcuts import render

class CustPasswordResetCompleteView(PasswordResetCompleteView):
    def get(self, request):
        return render(request,'password_reset_complete.html')