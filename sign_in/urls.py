from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/sign in
    path('', LoginView.as_view(template_name='sign_in/index.html'), name='sign_in-index'),
    path('logout', LogoutView.as_view(next_page='/homepage/'), name='logout')

]
