from django import forms
from .models import Product, Category

class UpdatePriceForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['price']


class ColoredSheetSearchForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['width', 'thickness', 'color', 'color_code']