from django.forms import ModelForm, widgets
from account.models import Profile

class ProfileForm(ModelForm):

    class Meta:
        model = Profile
        db_table = 'profile'
        exclude = ['id', 'user']
        widgets = {
            'favorite_cereal': widgets.Select(attrs={'class': 'form-control'}),
            'profile_image': widgets.TextInput(attrs={'class': 'form-control'})
        }