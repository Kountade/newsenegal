from django.urls import path
from tech import views
urlpatterns = [
    path("", views.home, name="home"),
    path("blogs", views.blogs, name="blogs"),
    path("services", views.service, name="services"),
    path("pricing", views.pricing, name="pricing"),
    path("contact", views.contact, name="contact"),
    path("blogs/blogdetail/<str:title>", views.blogdetail, name="blogdetail"),
    path("register", views.register, name="register"),


]
