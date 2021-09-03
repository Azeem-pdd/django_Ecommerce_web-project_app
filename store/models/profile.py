from store.models.customer import Customer
from django.db import models
from .customer import Customer
class Profile(models.Model):
    name  = models.CharField(max_length=20)
    profession = models.CharField(max_length=20)
    img = models.ImageField(upload_to='profile/%y', null=True, blank=True)
    job_position = models.CharField(max_length=40)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    phno = models.BigIntegerField(default=00000000000)
    home_address = models.TextField(default="")
    shipping_address = models.TextField(default="")
    postal_address = models.TextField(default="")
    zip_code = models.IntegerField(default=0, null=True)

    def __str__(self):
        return self.name
    @staticmethod
    def whether_customer_exists(customer):
        return Profile.objects.filter(customer = customer).first()
    

