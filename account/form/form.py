from django.forms import ModelForm, widgets
from account.models import Profile

class imageForm(ModelForm):

    class Meta:
        model = Profile
        db_table = 'profile'
        exclude = ['id']
        widgets = {
            'image': widgets.FileInput(attrs={'class': 'form-control'}),
        }