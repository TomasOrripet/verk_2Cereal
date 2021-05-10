from django.shortcuts import render, redirect
from cereal import models
from cereal.forms import cereal_form
from django.http import JsonResponse


def index(request):
    context = {'cereals': models.cereal.objects.all()}
    return render(request, 'cereal/index.html', context)


def createCereal(request):
    if request.method == 'POST':
        form = cereal_form.cerealCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('cereal-index')
    else:
        form = cereal_form.cerealCreateForm()
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

def updateItem(request):
    return JsonResponse('Item was added', safe=False)
