from django.urls import path
from . import views


urlpatterns = [
    #path('', views.index, name='account-index'),
    path('<int:id>', views.user_views, name='account_info')
]