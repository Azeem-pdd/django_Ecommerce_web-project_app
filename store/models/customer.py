from django.db import models
from datetime import datetime
class Customer(models.Model):
    
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phno = models.BigIntegerField(unique=True)
    password = models.CharField(max_length=200)
    confirm_password = models.CharField(max_length=200)
    last_login=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.first_name +" "+ self.last_name

    @staticmethod
    def email_exists(Email):
        if Customer.objects.filter(email = Email):
            return True
        else:
            return False
    def phno_exists(phno):
        if Customer.objects.filter(phno = phno):
            return True
        else:
            return False

    def is_email_valid(Email):
        try:
            return Customer.objects.get(email=Email)
        except:
            return False
    def get_cust_by_email(email):
        return Customer.objects.get(email=email)