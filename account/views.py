from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from account.form.form import profileForm
from account.models import Profile
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User


@login_required
def profile(request):
    profile = User.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = profileForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('userInfo')
    return render(request, 'account/userInfo.html',{
        'form':profileForm(instance=profile)
    })

# Create your views here.
@login_required
def index(request):
    return render(request, 'account/index.html')


@login_required
def user_views(request, id):
    content = {"user": get_object_or_404(User, id=id)}
    if request.user.id == id:
        return render(request, 'account/userInfo.html', content)
    return redirect('homepage-index')
