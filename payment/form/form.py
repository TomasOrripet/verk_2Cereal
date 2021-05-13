from payment.models import userInfo, cardInfo
from django.forms import ModelForm, widgets

class cardForm(ModelForm):

    class Meta:
        model = cardInfo
        exclude = ['id']
        fields = ['cardNumber','nameOfCardholder','expirationsDate','CVC',]

class userInfoForm(ModelForm):
    class Meta:
        model = userInfo
        exclude = ['id']
        fields = ['country', 'city', 'address', 'zip', ]