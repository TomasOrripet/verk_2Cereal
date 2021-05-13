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
