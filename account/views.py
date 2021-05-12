from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from account.form.form import imageForm
from account.models import Profile
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User


@login_required
def ImageForm(request, id):
    if request.method == 'POST':
        form = imageForm(data=request.POST)
        if form.is_valid():
            form.save()
            content = {"user": get_object_or_404(User, id=id)}
            return render(request, 'account/userInfo.html', content)
    else:
        form = imageForm()
    return render(request, 'userInfo.html', {
        'form': form
    })

# Create your views here.
@login_required
def index(request):
    return render(request, 'account/index.html')


@login_required
def user_views(request, id):
    content = {"user": get_object_or_404(User, id=id)}
    return render(request, 'account/userInfo.html', content)
