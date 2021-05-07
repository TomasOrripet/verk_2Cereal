from django.shortcuts import render, redirect

from cereal.forms import cereal_form


def index(request):
    return render(request, 'cereal/index.html')


def createCereal(request):
    if request.method == 'POST':
        form = cereal_form.cerealCreateForm(data=request.POST)
        if form.is_valid():
            cereal = form.save()
            return redirect('cereal-index')
    else:
        form = cereal_form.cerealCreateForm()
    return render(request, 'cereal/createCereal.html', {
        'form': form
    })

def createType(request):
    if request.method == 'POST':
        form = cereal_form.cerealCreateType(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('cereal-index')
    else:
        form = cereal_form.cerealCreateForm()
    return render(request, 'cereal/createType.html', {
        'form': form
    })

