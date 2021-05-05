from django.shortcuts import render, redirect
from django.http import HttpResponse

from sign_up.forms.sign_up_forms import createAccountForm


def index(request):
    return render(request, 'sign_up/index.html')

def createAccount(request):
    if request.method == 'POST':
        form = createAccountForm(data=request.POST)
        if form.is_valid():
            cereal = form.save()
            return redirect('account-index')
    else:
        form = createAccountForm()
    return render(request, 'sign_up', {
        'form': form
    })