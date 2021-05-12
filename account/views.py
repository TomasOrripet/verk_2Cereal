from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from account.form.form import profileForm
from account.models import Profile
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User

# Create your views here.
@login_required
def index(request):
    content = {"user": get_object_or_404(User, id=request.user.id)}
    return render(request, 'account/userInfo.html', content)


