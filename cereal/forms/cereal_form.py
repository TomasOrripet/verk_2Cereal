from django.forms import ModelForm, widgets
from cereal.models import cereal, type, manufacturer



class cerealForm(ModelForm):

    class Meta:
        model = cereal
        db_table = 'cereal'
        exclude = ['id']
        widgets = {
            'cerealName': widgets.TextInput(attrs={'class': 'form-control'}),
            'cerealContents': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'amountInStock': widgets.NumberInput(attrs={'class': 'form-control'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control'}),
            'image': widgets.TextInput(attrs={'class': 'form-control'}),
        }

class cerealCreateType(ModelForm):

    class Meta:
        model = type
        db_table = 'type'
        exclude = ['id']
        widgets = {
            'typeName': widgets.TextInput(attrs={'class': 'form-control'}),
        }


class cerealCreateManufacturer(ModelForm):

    class Meta:
        model = manufacturer
        db_table = 'manufacturer'
        exclude = ['id']
        widgets = {
            'manufacturerName': widgets.TextInput(attrs={'class': 'form-control'}),
        }
