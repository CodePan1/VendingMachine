from django.db import models


# Create your models here.
class VendingMachine(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    vending_machine = models.ForeignKey(VendingMachine, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    stock = models.DecimalField(max_digits=3)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name
