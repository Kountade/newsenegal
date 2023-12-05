from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User

# Create your views here.


def home(request):
    myservice = Services.objects.all()
    myrewies = Reviews.objects.all()
    myblog = Blogs.objects.all()

    context = {
        "myservice": myservice,
        "myrewies": myrewies,
        "myblog": myblog
    }

    return render(request, "solution/home.html", context,)


def blogs(request):
    myblog = Blogs.objects.all()
    context = {
        "myblog": myblog
    }
    return render(request, "solution/blogs.html", context)


def blogdetail(request, title: str):
    try:
        blogdetaile = Blogs.objects.get(title=title)

    except Blogs.DoesNotExist:
        raise ("le poste n'excite pas")
    return render(request, "solution/blogdetail.html", {"blogdetaile": blogdetaile})


def service(request):

    myservice = Services.objects.all()

    context = {
        "myservice": myservice
    }

    return render(request, "solution/services.html", context)


def pricing(request):
    myprising = Pricings.objects.all()

    context = {
        "myprising": myprising
    }

    return render(request, "solution/pricing.html", context)


def reviews(request):
    myrewies = Reviews.objects.all()

    context = {
        "myrewies": myrewies
    }
    return render(request, "solution/pages/home.html", context)


def contact(request):
    return render(request, "solution/contact.html")


def login(request):
    return render(request, "solution/login.html")


def register(request):
    return render(request, "solution/register.html")
