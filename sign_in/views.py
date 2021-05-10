from django.shortcuts import render
from sign_up.models import userAndPassword
# Create your views here.
def index(request):
    return render(request, 'sign_in/index.html')


