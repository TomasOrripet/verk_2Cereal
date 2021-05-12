from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from account.form.form import ImageForm
from django.contrib.auth.models import User

def image_upload_view(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            profilePic = form.instance
            return render(request, 'userInfo', {'form': form, 'profilePic': profilePic})
    else:
        form = ImageForm()
    return render(request, 'index.html', {'form': form})

# Create your views here.
@login_required
def index(request):
    return render(request, 'account/index.html')


@login_required
def user_views(request, id):
    content = {"user": get_object_or_404(User, id=id)}
    return render(request, 'account/userInfo.html', content)
