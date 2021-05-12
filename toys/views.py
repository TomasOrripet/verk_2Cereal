from django.shortcuts import render, redirect
from toys.forms import toyForms


# Create your views here.
def index(request):
    return render(request, "toys/index.html")



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
