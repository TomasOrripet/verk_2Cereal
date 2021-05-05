from django.forms import ModelForm, widgets
from cereal.models import Cereal



class cerealCreateForm(ModelForm):
    class Meta:
        model = Cereal
        db_table = 'Cereal'
        exclude = ['id']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'info': widgets.TextInput(attrs={'class': 'form-control'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control'}),
        }
