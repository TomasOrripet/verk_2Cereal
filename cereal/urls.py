from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/sign in
    path('', views.index, name='cereal-index'),
    path('createManufacturer', views.createManufacturer, name='createManufacturer'),
    path('cereal', views.cereal, name="cereal"),
    path('update_item', views.update_item, name='update_item    ')
]
