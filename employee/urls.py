from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('workers', views.workers, name='workers'),
  path('about-us', views.aboutUs, name='about-us')
]