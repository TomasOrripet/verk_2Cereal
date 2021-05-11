from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from account.models import Profile



# Create your views here.
@login_required
def index(request):
    return render(request, 'account/index.html')


@login_required
def user_views(request, id):
    content = {"user": get_object_or_404(Profile, user_id=id)}
    return render(request, 'account/userInfo.html', content)
