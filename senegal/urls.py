from django.urls import path
from senegal import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('new', views.news, name='new-page'),
    path('politique', views.politique, name='politique-page'),


]
