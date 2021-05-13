from django.shortcuts import render, redirect, get_object_or_404
from toys.forms import toyForms
from toys.models import toys


# Create your views here.
def index(request):
    context = {'toys': toys.objects.all()}
    return render(request, 'toys/index.html', context)



def CreateToy(request):
    if request.method == 'POST':
        form = toyForms.toyForms(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('toys-index')
        else:
            form = toyForms.toyForms()
        return render(request, 'toys/createToys.html', {
            'form': form
        })


def toyInfo(request, id):
    context = {'toys': get_object_or_404(toys, pk=id)}
    return render(request, 'toys/toysInfo.html', context)

def orderByPrice(request):
    if request.method == 'POST':
        query = request.POST['orderby']
        if query == 'name_a_z':
            context = {'toys': toys.objects.order_by('toyName')}
        elif query == 'name_z_a':
            context = {'toys': toys.objects.order_by('-toyName')}
        elif query == 'price_from_low':
            context = {'toys': toys.objects.order_by('price')}
        elif query == 'price_from_high':
            context = {'toys': toys.objects.order_by('-price')}
        return render(request, 'toys/index.html', context)

def searchResultToysView(request):
    query = request.POST['search']
    context = {'toys': toys.objects.filter(toyName__icontains=query)}
    return render(request, 'toys/index.html', context)
