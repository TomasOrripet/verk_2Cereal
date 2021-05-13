from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from account.form.form import ProfileForm
from account.models import Profile
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User

# Create your views here.
@login_required
def index(request):
    content = {"user": get_object_or_404(User, id=request.user.id)}
    return render(request, 'account/userInfo.html', content)
@login_required
def profile(request):
    profile = Profile.objects.filter(user=request.user).first
    if request.method == 'POST':
        form = ProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    return render(request, 'account/userInfo.html',{
        'form': ProfileForm(instance=Profile)
    })


