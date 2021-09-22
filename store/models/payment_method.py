from django.db import models

class Payment_method(models.Model):
    name = models.CharField(max_length=20)
    desc = models.CharField(max_length=150, default='')
    img = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.name
    @staticmethod
    def get_all_payemnt_methods():
        return Payment_method.objects.all()
    @staticmethod
    def get_payemnt_method_by_id(id):
        return Payment_method.objects.filter(id = id)
    