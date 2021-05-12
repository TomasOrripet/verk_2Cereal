from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    #path('', views.index, name='account-index'),
    path('<int:id>', views.user_views, name='account_info'),
    path('profile', views.profile, name='profile')
]+static(settings.MEDIA_URL, document_root= settings.MEDIA_URL)