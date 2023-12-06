from django.urls import path
from tech import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('new', views.news, name='new-page'),
    path('politique', views.politique, name='politique-page'),
    path('bussness', views.business, name='bussness-page'),
    path('blogs', views.blogsene, name='blogs-page'),


]
