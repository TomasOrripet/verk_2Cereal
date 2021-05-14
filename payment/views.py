from django.shortcuts import render, redirect
from payment.models import *
from cart.models import userCart
from payment.form.form import userInfoForm, cardForm
# Create your views here.
def index(request,):
    content = {
        'incart': userCart.objects.filter(user_id=request.user.id),
        'cardInfo': cardInfo.objects.filter(user_id=request.user.id),
        'contactInfo': userInfo.objects.filter(user_id=request.user.id)
    }
    return render(request, 'payment/index.html', content)

def cardInf(request):
    card = cardInfo.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = cardForm(data=request.POST, instance=card)
        if form.is_valid():
            card = form.save(commit=False)
            card.user = request.user
            card.save()
            return redirect('payment-index')
    else:
        form = cardForm()
        return render(request, 'payment/cardInfo.html', {
            'form': form
    })

def contactInfo(request):
    contact = userInfo.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = userInfoForm(data=request.POST, instance=contact)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            return redirect('cardInfo')
    else:
        form = userInfoForm()
        return render(request, 'payment/contactInfo.html',{
            'form': form
        })
