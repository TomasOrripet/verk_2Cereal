from django.forms import ModelForm, widgets
from cart.models import userCart

class CartForm(ModelForm):

    class Meta:
        model = userCart
        db_table = 'cart'
        exclude = ['id', 'user']
        widgets = {
            'cereal': widgets.TextInput(attrs={'class': 'form-control'}),
            'quantity': widgets.Select(attrs={'class': 'form-control'}),
        }


