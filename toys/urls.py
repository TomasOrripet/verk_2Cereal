from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/toys
    path('', views.index, name='toys-index'),
    path('<int:id>', views.toyInfo, name='toy_info'),
    path('priceResultToys', views.orderByPrice, name='priceResultToys'),
    path('searchResultToys', views.searchResultToysView, name='searchResultToys')
    #path('createtoy', views.toys, name='create-toy')
]