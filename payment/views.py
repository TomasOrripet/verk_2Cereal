from django.shortcuts import render, redirect
from cart.forms.cartForms import CartForm
from payment.models import *
from cart.models import userCart,toyCart
from payment.form.form import userInfoForm, cardForm
# Create your views here.
def index(request,):
    if request.method == 'POST':
        cardInfo.objects.filter(user=request.user).delete()
        userInfo.objects.filter(user=request.user).delete()
        userCart.objects.filter(user_id=request.user).delete()

#        card.delete()
#        contact.delete()
#        cart.delete()
        return redirect('homepage-index')
    else:
        content = {
            'incart': userCart.objects.filter(user_id=request.user.id),
            'toycart': toyCart.objects.filter(user_id=request.user.id),
            'cardInfo': cardInfo.objects.filter(user_id=request.user.id),
            'contactInfo': userInfo.objects.filter(user_id=request.user.id),
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
            print('ass')
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

def confirmation(request):
    return render(request, 'payment/confirmation.html')

