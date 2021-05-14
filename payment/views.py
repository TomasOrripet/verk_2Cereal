from django.shortcuts import render, redirect
from cart.forms.cartForms import CartForm
from cereal.models import cereal
from toys.models import toys
from payment.models import *
from cart.models import userCart, toyCart
from payment.form.form import userInfoForm, cardForm
# Create your views here.
def removeFromStock(id, amount):
    mycereal = cereal.objects.filter(pk=id).values()
    stock = (mycereal[0]['amountInStock'])
    mycereal.update(amountInStock=stock - amount)

def removeFromStockToys(id, amount):
    mytoys = toys.objects.filter(pk=id).values()
    stock = (mytoys[0]['amountInStock'])
    mytoys.update(amountInStock=stock - amount)



def index(request,):
    if request.method == 'POST':
        cerealcart = userCart.objects.filter(user_id=request.user).values()
        for anycereal in cerealcart:
            removeFromStock(anycereal['cereal_id'], anycereal['quantity'])
        toyscart = toyCart.objects.filter(user_id=request.user).values()
        for anytoys in toyscart:
            removeFromStockToys(anytoys['toy_id'], anytoys['quantity'])

        cardInfo.objects.filter(user=request.user).delete()
        toyCart.objects.filter(user=request.user).delete()
        userInfo.objects.filter(user=request.user).delete()
        userCart.objects.filter(user_id=request.user).delete()
        toyCart.objects.filter(user_id=request.user).delete()

        return redirect('confirmation')
    else:
        total = 0
        toys = toyCart.objects.filter(user_id=request.user.id).values()
        for toy in toys:
            total += toy['price'] * toy['quantity']
        cereals = userCart.objects.filter(user=request.user).values()
        for cereal in cereals:
            total += cereal['price'] * cereal['quantity']
        content = {
            'incart': userCart.objects.filter(user_id=request.user.id),
            'toycart': toyCart.objects.filter(user_id=request.user.id),
            'cardInfo': cardInfo.objects.filter(user_id=request.user.id),
            'contactInfo': userInfo.objects.filter(user_id=request.user.id),
            'total': total,
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
            return render(request, 'payment/contactInfo.html', {
                'form': form
            })
    else:
        form = userInfoForm()
        return render(request, 'payment/contactInfo.html',{
            'form': form
        })
def confirmation(request):
    if request.method == 'POST':
        return redirect('homepage-index')
    else:
        return render(request, 'payment/confirmation.html')

