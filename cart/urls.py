from django.urls import path
from . import views


urlpatterns = [
    #http://localhost:8000/Homepage/cart
    path('', views.index, name='cart-index'),
    path('<int:id>', views.addToCart, name='cart-add')
]