from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/sign in
    path('', views.index, name='cereal-index'),
    path('createCereal', views.createCereal, name="createCereal")
]
