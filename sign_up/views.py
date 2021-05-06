from django.shortcuts import render, redirect
from django.http import HttpResponse

from sign_up.forms.sign_up_forms import createAccountForm
from sign_up.models import createAccountImage, userAndPassword


def index(request):
    return render(request, 'sign_up/index.html')

def info(request):
    if request.method == 'POST':
        form = createAccountForm(data=request.POST)
        if form.is_valid():
            account = form.save()
            user = userAndPassword(username=request.POST['username'], password=request.POST['password'], account=account)
            user.save()
            inf_image = createAccountImage(image=request.POST['image'], account=account)
            inf_image.save()
            return redirect('account-index')
    else:
        form = createAccountForm()
    return render(request, 'sign_up/info.html', {
        'form': form
    })