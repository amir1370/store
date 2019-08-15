from django import forms
from .models import Product, Category

class UpdatePriceForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['price']


class SheetSearchForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['width', 'thickness']