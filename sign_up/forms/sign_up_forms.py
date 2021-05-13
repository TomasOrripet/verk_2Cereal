from django.forms import ModelForm, widgets
from django import forms
from sign_up.models import createAccount


class createAccountForm(ModelForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = createAccount
        db_table = 'sign_up'
        exclude = ['id', 'country', 'city', 'address', 'zip']
        widgets = {
            'first_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'last_name': widgets.TextInput(attrs={'class': 'form-control'}),
        }




