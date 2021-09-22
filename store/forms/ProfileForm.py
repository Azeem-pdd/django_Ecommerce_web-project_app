from django import forms
from django.forms import ModelForm, fields
from django.http import request
from ..models.profile import Profile

class ProfileForm(ModelForm):
    
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['customer']
        

        