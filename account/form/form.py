from django.forms import ModelForm, widgets
from account.models import Profile

class profileForm(ModelForm):

    class Meta:
        model = Profile
        db_table = 'profile'
        exclude = ['id', 'user']
        widgets = {
            'image': widgets.FileInput(attrs={'class': 'form-control'}),
        }