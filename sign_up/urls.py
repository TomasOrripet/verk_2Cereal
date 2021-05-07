from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/sign in
    path('', views.index, name='sign_up-index'),
    path('info', views.info, name="info"),
    path('register/', views.register, name="register")
]