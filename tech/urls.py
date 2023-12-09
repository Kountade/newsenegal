from django.urls import path
from tech import views
from django.conf.urls import handler404

from tech.views import custom_404

handler404 = custom_404


urlpatterns = [
    path('', views.home, name='home-page'),
    path('politiques', views.politique, name='politique-page'),
    path('sports', views.sports, name='sports-page'),
    path('bussness', views.business, name='bussness-page'),
    path('blogs', views.blogsene, name='blogs-page'),
    # path('newsdetail/<str:title>', views.newsdetail, name="newsdetail-page"),
    path('home/<path:news_title>/',
         views.home_detail, name='home_detail'),
    path('politique/<path:news_title>/',
         views.politique_detail, name='politique_detail'),
    path('sport/<path:news_title>/',
         views.sports_detail, name='sport_detail'),
]
