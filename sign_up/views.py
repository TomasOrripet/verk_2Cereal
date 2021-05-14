from django.db import IntegrityError
from django.shortcuts import render, redirect
from sign_up.forms.sign_up_forms import createAccountForm
from django.contrib.auth.models import User

def index(request):
    return render(request, 'sign_up/index.html')

def info(request):
    if request.method == 'POST':
        form = createAccountForm(data=request.POST)
        if form.is_valid():
            try:
                user = User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password'],
                    first_name=request.POST['first_name'],
                    last_name=request.POST['last_name'],
                )
                user.save()
            except IntegrityError:
                return render(request, 'sign_up/info.html', {
                    'form': form,
                    'username': 'this Username is taken'
                })
            return redirect('homepage-index')
    else:
        form = createAccountForm()
    return render(request, 'sign_up/info.html', {
        'form': form
    })
