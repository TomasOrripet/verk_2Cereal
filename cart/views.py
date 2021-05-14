import json

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from cart.models import *
# Create your views here.
def index(request):
    content = {'incart': userCart.objects.filter(user_id=request.user.id),
               'toyincart': toyCart.objects.filter(user_id=request.user.id)}
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            if data['amount'] == 1:
                userCart.objects.filter(user=request.user, cereal_id=data['cerealid']).delete()
            else:
                userCart.objects.update(quantity=data['amount']-1)
        except:
            if data['amount'] == 1:
                toyCart.objects.filter(user=request.user, toy_id=toyCart.toy.id).delete()
            else:
                userCart.objects.update(quantity=data['amount']-1)


        return render(request, 'cart/index.html', content)

    return render(request, 'cart/index.html', content)


