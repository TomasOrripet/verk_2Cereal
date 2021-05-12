from django.forms import ModelForm
from account.models import Profile

class ImageForm(ModelForm):
    """Form for the image model"""
    class Meta:
        model = Profile
        fields = ["image"]