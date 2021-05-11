from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/sign in
    path('', views.info, name="info"),
    path('register/', views.register, name="register")
]