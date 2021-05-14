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
            item = userCart.objects.filter(user=request.user, cereal_id=data['cerealid'])
            if data['amount'] == 1:
                item.delete()
                print(3)
                userCart.objects.filter(user=request.user, cereal_id=data['cerealid']).delete()
            else:

                print(2)
                item.update(quantity=data['amount']-1)
        except:
            item = toyCart.objects.filter(user=request.user, toy_id=data['toyid'])
            if data['amount'] == 1:
                print(1)
                item.delete()
            else:
                item.update(quantity=data['amount']-1)

        return JsonResponse("done", safe=False)

    return render(request, 'cart/index.html', content)


