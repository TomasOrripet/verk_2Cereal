from django.shortcuts import render, redirect
from django.http import HttpResponse
from cart.models import *
# Create your views here.
def index(request,):
    if request.method == 'POST':
        try:
            userCart.objects.filter(user=request.user, cereal_id=userCart.cereal.id).delete()
        except:
            toyCart.objects.filter(user=request.user, toy_id=toyCart.toy.id).delete()
    content = {'incart': userCart.objects.filter(user_id=request.user.id),
               'toyincart': toyCart.objects.filter(user_id=request.user.id)}
    return render(request, 'cart/index.html', content)


