from django.contrib.auth.views import PasswordResetDoneView

from django.shortcuts import render

class CustPasswordResetDoneView(PasswordResetDoneView):
    def get(self, request):
        return render(request, 'password_reset_done.html')