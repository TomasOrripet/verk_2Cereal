from django.forms import ModelForm, widgets
from cereal.models import createCereal, createType



class cerealCreateForm(ModelForm):

    class Meta:
        model = createCereal
        db_table = 'cereal'
        exclude = ['id']
        widgets = {
            'cerealName': widgets.TextInput(attrs={'class': 'form-control'}),
            'cerealNutritionalValue': widgets.TextInput(attrs={'class': 'form-control'}),
            'cerealContents': widgets.TextInput(attrs={'class': 'form-control'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control'}),
        }

class cerealCreateType(ModelForm):

    class Meta:
        model = createType
        db_table = 'type'
        exclude = ['id']
        widgets = {
            'typeName': widgets.TextInput(attrs={'class': 'form-control'}),
        }
