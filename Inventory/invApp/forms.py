from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels =  {
            'product_id': 'Product ID',
            'name': 'Product Name',
            'sku': 'SKU',
            'price': 'Price',
            'quantity': 'Quantity',
            'supplier': 'Supplier',
        }
        widgets = {
            'product_id': forms.TextInput(attrs={'placeholder': 'Enter Product ID', 'class': 'form-control'}),
            'name': forms.TextInput(attrs={'placeholder': 'Enter Product Name', 'class': 'form-control'}),
            'sku': forms.TextInput(attrs={'placeholder': 'Enter SKU', 'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Enter Price', 'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'placeholder': 'Enter Quantity', 'class': 'form-control'}),
            'supplier': forms.TextInput(attrs={'placeholder': 'Enter Supplier', 'class': 'form-control'}),
            }