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
def filterBy(request):
    if request.method == 'POST':
        query2 = request.POST['manufacturer']
        if query2 == 'none':
            context2 = toys.objects.filter(manufacturer__manufacturerName__contains=query2)

        else:
            context2 = toys.objects.filter(manufacturer__manufacturerName__contains=query2)

        list1 = []
        list2 = []
        querySet2 = toys.objects.none()
        for i in context2:
            list2.append(i)
        for j in context1:
            list1.append(j)
        if len(list1) != 0 and len(list2) != 0:
            for x in list1:
                if x in list2:
                    querySet1 = toys.objects.filter(toyName__icontains=x)
                    querySet2 = querySet2 | querySet1
            finaContext = {'toys': querySet2}
            return render(request, 'toys/index.html', finaContext)
        else:
            for i in list1, list2:
                for x in i:
                    querySet1 = toys.objects.filter(toyName__icontains=x)
                    querySet2 = querySet2 | querySet1
            finaContext = {'toys': querySet2}
            return render(request, 'toys/index.html', finaContext)

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
