from django.shortcuts import render
from django.http import HttpResponse
from cart.models import *
# Create your views here.
def index(request,):
    content = {'incart': order.objects.all()}
    return render(request, 'cart/index.html', content)


