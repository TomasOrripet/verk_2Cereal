from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/sign in
    path('', views.index, name='cereal-index'),
    path('createType', views.createType, name='createType'),
    path('createCereal', views.createCereal, name="createCereal"),
    path('update_item', views.updateItem, name='update_item')
]
