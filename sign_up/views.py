

from django.shortcuts import render, redirect
from account.models import Profile
from sign_up.forms.forms import RegisterForm
from sign_up.forms.sign_up_forms import createAccountForm
from django.contrib.auth.models import User


def index(request):
    return render(request, 'sign_up/index.html')

def info(request):
    if request.method == 'POST':
        form = createAccountForm(data=request.POST)
        try:
            if form.is_valid():
                user = User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password'],
                    first_name=request.POST['first_name'],
                    last_name=request.POST['last_name'],
                )
                user.save()
                return redirect('homepage-index')
        except:
            form = createAccountForm()
            return render(request, 'sign_up/info.html', {
                'form': form
            })
    else:
        form = createAccountForm()
    return render(request, 'sign_up/info.html', {
        'form': form
    })

def register(response):
    if response.method == 'POST':
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
    else:
        form = RegisterForm()
    return render(response, "sign_up/register.html", {"form":form})