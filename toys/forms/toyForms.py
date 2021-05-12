from django.forms import ModelForm, widgets
from toys.models import toys

class toyForms(ModelForm):

    class Meta:
        model = toys
        db_table = 'toys'
        exclude = ['id']
        widgets = {
            'toyName': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control'}),
            'amountInStock': widgets.NumberInput(attrs={'class': 'form-control'}),
            'type': widgets.TextInput(attrs={'class': 'form-control'}),
            'image': widgets.TextInput(attrs={'class': 'form-control'}),
            'manufacturer': widgets.TextInput(attrs={'class': 'form-control'}),
        }
