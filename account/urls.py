from django.urls import path
from . import views
from account import views as user_views


urlpatterns = [
    # http://localhost:8000/toys
    path('', views.index, name='account-index'),
    path('profile/', user_views.index, name='account-index')
]