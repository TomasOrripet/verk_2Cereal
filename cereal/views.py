from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from cart.forms import cartForms
from cart.models import cereal, userCart
from cereal.forms import cereal_form
from django.http import JsonResponse
import json

def index(request):
    context = {'cereals': cereal.objects.all()}
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

"""
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
"""


def cerealInfo(request, id):
    context = {'cereal': get_object_or_404(cereal, pk=id)}
    return render(request, 'cereal/cerealInfo.html', context)

@login_required
def updateItem(request):
    data = json.loads(request.body)
    cerealName = data['cerealName']
    cerealId = data['cerealId']
    cerealprice = data['price']
    action = data['action']

    cart = userCart.objects.filter(user_id=request.user.id)
    update = cart.filter(cereal_id=cerealId)
    values = update.values()
    try:
        total = values[0]['quantity']
        update.update(quantity=(total+1))
        print(update)

    except:
        print("inzero")
        add = userCart.objects.create(
            user_id=request.user.id,
            cereal_id=cerealId
        )
        add.save()
    return JsonResponse("Item was added", safe=False)

def searchResultCerealView(request):
    query = request.POST['search']
    context = {'cereals': cereal.objects.filter(cerealName__icontains=query)}
    return render(request, 'cereal/index.html', context)

def orderByPrice(request):
    if request.method == 'POST':
        query = request.POST['orderby']
        if query == 'name_a_z':
            context = {'cereals': cereal.objects.order_by('cerealName')}
        elif query == 'name_z_a':
            context = {'cereals': cereal.objects.order_by('-cerealName')}
        elif query == 'price_from_low':
            context = {'cereals': cereal.objects.order_by('price')}
        elif query == 'price_from_high':
            context = {'cereals': cereal.objects.order_by('-price')}
        return render(request, 'cereal/index.html', context)

def filterBy(request):
    if request.method == 'POST':
        query1 = request.POST['type']
        query2 = request.POST['manufacturer']
        if query2 == 'none':
            context2 = cereal.objects.filter(manufacturer__manufacturerName__contains=query2)

        else:
            context2 = cereal.objects.filter(manufacturer__manufacturerName__contains=query2)


        if query1 == 'Healthy':
            context1 = cereal.objects.filter(type_id=1)

        elif query1 == 'Sugary':
            context1 = cereal.objects.filter(type_id=2)

        else:
            context1 = cereal.objects.filter(type_id=0)
        list1 = []
        list2 = []
        querySet2 = cereal.objects.none()
        for i in context2:
            list2.append(i)
        for j in context1:
            list1.append(j)
        if len(list1) != 0 and len(list2) != 0:
            for x in list1:
                if x in list2:
                    querySet1 = cereal.objects.filter(cerealName__icontains=x)
                    querySet2 = querySet2 | querySet1
            finaContext = {'cereals': querySet2}
            return render(request, 'cereal/index.html', finaContext)
        else:
            for i in list1, list2:
                for x in i:
                    querySet1 = cereal.objects.filter(cerealName__icontains=x)
                    querySet2 = querySet2 | querySet1
            finaContext = {'cereals': querySet2}
            return render(request, 'cereal/index.html', finaContext)
