from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/sign in
    path('', views.index, name='sign_up-index'),
    path('createAccount', views.createAccount, name="createAccount")
]