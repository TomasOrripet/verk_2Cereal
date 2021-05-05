from django.shortcuts import render, redirect

from cereal.forms.cereal_form import cerealCreateForm


def index(request):
    return render(request, 'cereal/index.html')


def createCereal(request):
    if request.method == 'POST':
        form = cerealCreateForm(data=request.POST)
        if form.is_valid():
            cereal = form.save()
            return redirect('cereal-index')
    else:
        form = cerealCreateForm()
    return render(request, 'cereal/createCereal.html', {
        'form': form
    })
