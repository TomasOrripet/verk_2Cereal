from payment.models import userInfo, cardInfo
from django.forms import ModelForm, widgets

class cardForm(ModelForm):

    class Meta:
        model = cardInfo
        exclude = ['id', 'user']
        widgets = {
            'cardNumber': widgets.NumberInput(attrs={'class': 'form-control'}),
            'nameOfCardholder': widgets.TextInput(attrs={'class': 'form-control'}),
            'expirationsDate': widgets.TextInput(attrs={'class': 'form-control'}),
            'CVC': widgets.NumberInput(attrs={'class': 'form-control'}),

        }

class userInfoForm(ModelForm):


    class Meta:
        country_choices = [(1, 'Iceland'), (2, 'Norway'), (3, 'Denmark'), (4, 'Istanbul'), (5,'Kazakhstan')]
        model = userInfo
        exclude = ['id', 'user']
        widgets = {
            'country': widgets.Select(choices=country_choices),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
            'address': widgets.TextInput(attrs={'class': 'form-control'}),
            'zip': widgets.NumberInput(attrs={'class': 'form-control'}),

        }
        fields = ['country', 'city', 'address', 'zip', ]