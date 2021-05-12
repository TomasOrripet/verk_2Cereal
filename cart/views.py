from django.shortcuts import render, redirect
from django.http import HttpResponse
from cart.models import *
# Create your views here.
def index(request,):
    content = {'incart': userCart.objects.filter(user_id=request.user.id)}
    return render(request, 'cart/index.html', content)

def addToCart(request, id):
    cart = userCart.objects.create(
        user_id=request.user.id,
        cereal_id=id
    )
    cart.save()
    return redirect('cereal-index')

