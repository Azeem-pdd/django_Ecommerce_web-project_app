from django.contrib.auth import tokens
from django.contrib.auth.views import PasswordResetView
from django.shortcuts import redirect, render
from ..forms.password_reset import UserPasswordResetForm
from ..models.customer import Customer
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context, context

class CustPasswordResetView(PasswordResetView):
    def get(self, request):
        context={}
        form=UserPasswordResetForm()
        context['form']=form
        return render(request, 'password_reset.html',context)
    def post(self, request):
        form=UserPasswordResetForm(request.POST or None)
        if form.is_valid():
            email=form.cleaned_data['email']
            if Customer.get_cust_by_email(email):
                context={}
                user=Customer.get_cust_by_email(email)
                token=default_token_generator.make_token(user)
                get_temp=get_template('password_reset_email.html')
                context['token']=token
                context['cust']=user
                html_content=get_temp.render(context)
                subject='Password Reset on 127.0.0.1'
                message='have you requested password change on 127.0.0.1:8080'
                recipient_list=[email]
                from_email=settings.EMAIL_HOST_USER
                email=EmailMultiAlternatives(subject, message, from_email, recipient_list)
                email.attach_alternative(html_content,"text/html")
                email.send()
                return redirect('password_reset_done')
            