from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/toys
    path('', views.index, name='cutlery-index'),
]