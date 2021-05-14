import json
from django.shortcuts import render, redirect
from cart.models import *
# Create your views here.
def index(request):

    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            item = userCart.objects.filter(user=request.user, cereal_id=data['cerealid'])
            if data['amount'] == 1:
                item.delete()
                userCart.objects.filter(user=request.user, cereal_id=data['cerealid']).delete()
            else:
                item.update(quantity=data['amount']-1)
        except:
            item = toyCart.objects.filter(user=request.user, toy_id=data['toyid'])
            if data['amount'] == 1:
                item.delete()
            else:
                item.update(quantity=data['amount']-1)

        return redirect('cart-index')
    else:
        total=0
        toys = toyCart.objects.filter(user_id=request.user.id).values()
        for toy in toys:
            total += toy['price']*toy['quantity']
        cereals = userCart.objects.filter(user=request.user).values()
        for cereal in cereals:
            total += cereal['price']*cereal['quantity']
        content = {'incart': userCart.objects.filter(user_id=request.user.id),
                   'toyincart': toyCart.objects.filter(user_id=request.user.id),
                   'total': total}

        return render(request, 'cart/index.html', content)




