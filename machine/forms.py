from django import forms
from .models import VendingMachine, Product


class VendingMachineForm(forms.ModelForm):
    class Meta:
        model = VendingMachine
        fields = ['name', 'location']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'stock', 'price']
