from django.urls import path
from . import views


urlpatterns = [
    #http://localhost:8000/Homepage/cart/payment
    path('', views.index, name='payment-index'),
]