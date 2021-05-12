from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/toys
    path('', views.index, name='toys-index'),
    #path('createtoy', views.toys, name='create-toy')
]