from django.shortcuts import render, redirect
from django.views.generic import ListView
from cart.models import orderCerealItem, order
from cereal.models import cereal
from cart import models
from cereal.forms import cereal_form
from django.http import JsonResponse
import json

def index(request):
    context = {'cereals': models.cereal.objects.all()}
    return render(request, 'cereal/index.html', context)


def Cereal(request):
    if request.method == 'POST':
        form = cereal_form.cerealForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('cereal-index')
    else:
        form = cereal_form.cerealForm()
    return render(request, 'cereal/createCereal.html', {
        'form': form
    })


def createManufacturer(request):
    if request.method == 'POST':
        form = cereal_form.cerealCreateManufacturer(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('cereal-index')
    else:
        form = cereal_form.cerealCreateManufacturer()
    return render(request, 'cereal/createType.html', {
        'form': form
    })



def cerealInfo(request):
    context = {'cereals': models.cereal.objects.all()}
    return render(request, 'cereal/cerealInfo.html', context)

def updateItem(request):
    data = json.loads(request.body)
    cerealName = data['cerealName']
    cerealId = data['cerealId']
    action = data['action']
    print('action:', action)
    print('cerealId:', cerealId)
    print('cerealName:', cerealName)
    if action == 'add' and orderCerealItem.quantity == 0:
        orderCerealItem.quantity = (orderCerealItem.quantity + 1)
    elif action == 'remove':
        orderCerealItem.quantity = (orderCerealItem.quantity - 1)
    return JsonResponse("Item was added", safe=False)

def searchResultCerealView(request):
    query = request.POST['search']
    context = {'cereals': cereal.objects.filter(cerealName__icontains=query)}
    return render(request, 'cereal/index.html', context)

def orderByPrice(request):
    context = {'cereals': cereal.objects.filter(cerealName__icontains='coco')}
    return render(request, 'cereal/index.html', context)

