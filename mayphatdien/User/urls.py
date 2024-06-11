from django.urls import path
from django.views.generic import TemplateView

from .views import register_request,login1
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path('login/', login1, name='login'),
    path('register/', register_request, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
  #  path('logout/',  TemplateView.as_view(template_name='login.html'),  name='logout'),


]
