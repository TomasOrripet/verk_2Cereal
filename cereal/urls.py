from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/sign in
    path('', views.index, name='cereal-index'),
    path('createManufacturer', views.createManufacturer, name='createManufacturer'),
    path('searchResult', views.searchResultCerealView, name='searchResult'),
    path('priceResult', views.orderByPrice, name='priceResult'),
    path('cereal', views.Cereal, name="cereal"),
    path('update_item', views.updateItem, name='update_item'),
    path('<int:id>', views.cerealInfo, name='cereal_info')
]
