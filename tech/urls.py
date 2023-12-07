from django.urls import path
from tech import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('new', views.news, name='new-page'),
    path('politiques', views.politique, name='politique-page'),
    path('bussness', views.business, name='bussness-page'),
    path('blogs', views.blogsene, name='blogs-page'),
    path('newsdetail/<str:title>', views.newsdetail, name="newsdetail-page"),
    path('politique/<path:news_title>/',
         views.politique_detail, name='politique_detail'),


]
