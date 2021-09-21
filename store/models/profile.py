from store.models.customer import Customer
from django.db import models
from .customer import Customer
class Profile(models.Model):
    name  = models.CharField(max_length=20, null=True)
    profession = models.CharField(max_length=20, null=True)
    img = models.ImageField(upload_to='profile/%y', null=True, blank=True)
    job_position = models.CharField(max_length=40, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    phno = models.BigIntegerField(default=00000000000, null=True)
    home_address = models.TextField(default="", null=True)
    shipping_address = models.TextField(default="", null=True)
    postal_address = models.TextField(default="", null=True)
    zip_code = models.IntegerField(default=0, null=True)

    def __str__(self):
        return self.name
    @staticmethod
    def whether_customer_exists(customer):
        return Profile.objects.filter(customer = customer).first()
    

