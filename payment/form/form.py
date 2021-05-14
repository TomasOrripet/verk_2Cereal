from payment.models import userInfo, cardInfo
from django.forms import ModelForm, widgets

class cardForm(ModelForm):

    class Meta:
        model = cardInfo
        exclude = ['id', 'user']
        widgets = {
            'cardNumber': widgets.NumberInput(attrs={'class': 'form-control', 'maxlength': '16'}),
            'nameOfCardholder': widgets.TextInput(attrs={'class': 'form-control'}),
            'expirationsDate': widgets.TextInput(attrs={'class': 'form-control'}),
            'CVC': widgets.NumberInput(attrs={'class': 'form-control', 'maxlength': '3'}),

        }

class userInfoForm(ModelForm):


    class Meta:
        country_choices = [(1, 'Iceland'), (2, 'Norway'), (3, 'Denmark'), (4, 'Istanbul'), (5,'Kazakhstan')]
        model = userInfo
        exclude = ['id', 'user']
        widgets = {
            'name': widgets.TextInput( attrs={'class': 'form-control'}),
            'country': widgets.Select(choices=country_choices,attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
            'address': widgets.TextInput(attrs={'class': 'form-control'}),
            'zip': widgets.NumberInput(attrs={'class': 'form-control'}),

        }