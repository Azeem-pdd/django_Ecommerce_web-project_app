from django.contrib.auth import forms
from django.contrib.auth.forms import PasswordResetForm, UsernameField
from django.forms.fields import EmailField
from ..models.customer import Customer
class UserPasswordResetForm(PasswordResetForm):
    email=EmailField(required=True,)
    class meta:
        model=Customer
        fields=['email']