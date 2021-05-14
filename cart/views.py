
from django.shortcuts import render
from cart.models import *
# Create your views here.


def index(request,):
    content = {'incart': userCart.objects.filter(user_id=request.user.id),
               'toyincart': toyCart.objects.filter(user_id=request.user.id)}
    return render(request, 'cart/index.html', content)
