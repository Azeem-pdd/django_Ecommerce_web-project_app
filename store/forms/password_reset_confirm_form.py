from django.contrib.auth.forms import SetPasswordForm
from django.forms import fields
from ..models.customer import Customer
from django import forms

class CustPasswordSetForm(SetPasswordForm, forms.Form):
    new_password=forms.CharField(label='new_password', max_length=30, widget=forms.PasswordInput)
    new_password_confirmation=forms.CharField(label='new_password_confirmation', max_length=30, widget=forms.PasswordInput)