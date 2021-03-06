from payment.models import userInfo, cardInfo
from django.forms import ModelForm, widgets

class cardForm(ModelForm):

    class Meta:
        model = cardInfo
        exclude = ['id', 'user']
        widgets = {
            'cardNumber': widgets.NumberInput(attrs={'class': 'form-control', 'placeholder': 'xxxx-xxxx-xxxx-xxxx'}),
            'nameOfCardholder': widgets.TextInput(attrs={'class': 'form-control'    }),
            'expirationsDate': widgets.TextInput(attrs={'class': 'form-control'}),
            'CVC': widgets.NumberInput(attrs={'class': 'form-control', 'maxlength': '3', 'placeholder': 'xxx'}),

        }

class userInfoForm(ModelForm):


    class Meta:
        country_choices = [('Iceland', 'Iceland'), ('Norway', 'Norway'), ('Denmark', 'Denmark'), ('Istanbul', 'Istanbul'), ('Kazakhstan', 'Kazakhstan')]
        model = userInfo
        exclude = ['id', 'user']
        widgets = {
            'name': widgets.TextInput( attrs={'class': 'form-control'}),
            'country': widgets.Select(choices=country_choices,attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
            'address': widgets.TextInput(attrs={'class': 'form-control'}),
            'zip': widgets.NumberInput(attrs={'class': 'form-control'}),

        }