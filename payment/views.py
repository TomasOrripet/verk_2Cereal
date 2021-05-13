from django.shortcuts import render, redirect
from django.http import HttpResponse
from payment.models import *
from payment.form.form import userInfoForm, cardForm
# Create your views here.
def index(request,):
    return render(request, 'payment/index.html')

def cardInfo(request):

    if request.method == 'POST':
        form = cardForm(data=request.POST)
        if form.is_valid():
            card = form.save(commit=False)
            card.user = request.user
            card.save()
            return redirect('/contactInfo')
    else:
        form = cardForm()
        return render(request, 'payment/cardInfo.html', {
            'form': form
    })

def contactInfo(request):
    contact = userInfo.objects.filter(user=request.user)
    if request.method == 'POST':
        form = userInfo(data=request.POST, instance=contact)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact .save()

    return render(request, 'payment/cardInfo.html',{
        'form': userInfoForm(instance=userInfoForm)
    })
