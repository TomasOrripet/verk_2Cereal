from django.shortcuts import render
from django.http import HttpResponse
from cart.models import *
# Create your views here.
def index(request,):
    return render(request, 'payment/index.html')


