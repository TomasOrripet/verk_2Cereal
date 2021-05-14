from django.forms import ModelForm, widgets
from cart.models import userCart,toyCart

class CartForm(ModelForm):

    class Meta:
        model = userCart
        db_table = 'cart'
        exclude = ['id', 'user']
        widgets = {
            'cereal': widgets.TextInput(attrs={'class': 'form-control'}),
            'quantity': widgets.Select(attrs={'class': 'form-control'}),
        }

class toyCartForm(ModelForm):

    class Meta:
        model = toyCart
        db_table = 'toycart'
        exclude = ['id', 'user']
        widgets = {
            'toy': widgets.TextInput(attrs={'class': 'form-control'}),
            'quantity': widgets.Select(attrs={'class': 'form-control'}),
        }

