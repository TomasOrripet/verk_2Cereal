from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/sign in
    path('', views.index, name='cereal-index'),
    path('createManufacturer', views.createManufacturer, name='createManufacturer'),
    path('cereal', views.cereal, name="cereal"),
    path('update_item', views.updateItem, name='update_item'),
    path('content', views.cerealInfo, name='cereal_info')
]
