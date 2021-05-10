from django.shortcuts import render
from django.http import HttpResponse
from cart.models import order

# Create your views here.
def index(request):
    return render(request, 'cart/index.html')


