from django.forms import ModelForm, widgets
from cereal.models import createCereal



class cerealCreateForm(ModelForm):
    class Meta:
        model = createCereal
        db_table = 'Cereal'
        exclude = ['id']
        widgets = {
            'cerealName': widgets.TextInput(attrs={'class': 'form-control'}),
            'cerealNutritionalValue': widgets.TextInput(attrs={'class': 'form-control'}),
            'cerealContents': widgets.TextInput(attrs={'class': 'form-control'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control'}),
        }
