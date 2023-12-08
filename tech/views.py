from django.shortcuts import render

# Create your views here.
import requests  # Importez requests pour effectuer des requêtes HTTP
from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def news(request):
 #   try:
    url = f'https://newsdata.io/api/1/news?country=sn&category=politics&apikey=pub_33467774e35656a9e0c14a93978036b649c82'
    response = requests.get(url)
    # Raise an exception for bad responses (4xx and 5xx status codes)
    response.raise_for_status()
    data = response.json()

    results = data["results"]
    # Add this line to inspect the structure of the data dictionary

    # Adjust the code based on the actual structure of the API response
    # Use get to provide a default empty list if 'articles' key is not present
   # articles = data.get('articles', [])

    context = {
        'results': results
    }
    return render(request, 'pages/news.html', context)

  #  except requests.exceptions.RequestException as e:
    # Handle request errors (e.g., network issues, API errors)
  #  context = {
#        'error_message': f"Error fetching news: {e}"
  #   :#   }
 #   return render(request, 'pages/error.html', context)


def home(request):
    url = f'https://newsdata.io/api/1/news?country=sn&apikey=pub_33467774e35656a9e0c14a93978036b649c82'
    response = requests.get(url)
    # Raise an exception for bad responses (4xx and 5xx status codes)
    response.raise_for_status()
    data = response.json()
    newsblog = blog.objects.all().order_by('-date')[:4]
    results = data["results"]

    context = {
        'results': results,
        'newsblog': newsblog,
    }

    return render(request, 'pages/index.html', context)


def sports(request):
    url = f'https://newsdata.io/api/1/news?country=sn&category=sports&apikey=pub_33467774e35656a9e0c14a93978036b649c82'
    response = requests.get(url)
    # Raise an exception for bad responses (4xx and 5xx status codes)
    response.raise_for_status()
    data = response.json()

    results = data["results"]

    context = {
        'results': results
    }

    return render(request, 'pages/sports.html', context)


def sports_detail(request, news_title):
    url = f'https://newsdata.io/api/1/news?country=sn&category=sports&apikey=pub_33467774e35656a9e0c14a93978036b649c82'
    response = requests.get(url)
    # Raise an exception for bad responses (4xx and 5xx status codes)
    response.raise_for_status()
    data = response.json()

    results = data["results"]

    # Trouver l'article spécifique par ID ou index
    specific_news = next(
        (news for news in results if news["title"] == news_title), None)
    context = {
        'specific_news': specific_news
    }

    return render(request, 'pages/sports_detail.html', context)


def politique(request):
    url = f'https://newsdata.io/api/1/news?country=sn&category=politics&apikey=pub_33467774e35656a9e0c14a93978036b649c82'
    response = requests.get(url)
    # Raise an exception for bad responses (4xx and 5xx status codes)
    response.raise_for_status()
    data = response.json()

    results = data["results"]

    context = {
        'results': results
    }

    return render(request, 'pages/politique.html', context)


def politique_detail(request, news_title):
    url = f'https://newsdata.io/api/1/news?country=sn&category=politics&apikey=pub_33467774e35656a9e0c14a93978036b649c82'
    response = requests.get(url)
    # Raise an exception for bad responses (4xx and 5xx status codes)
    response.raise_for_status()
    data = response.json()

    results = data["results"]

    # Trouver l'article spécifique par titre
    specific_news = next(
        (news for news in results if news["title"] == news_title), None)

    context = {
        'specific_news': specific_news
    }

    return render(request, 'pages/politique_detail.html', context)


def business(request):
    url = f'https://newsdata.io/api/1/news?country=sn&category=business&apikey=pub_33467774e35656a9e0c14a93978036b649c82'
    response = requests.get(url)
    # Raise an exception for bad responses (4xx and 5xx status codes)
    response.raise_for_status()
    data = response.json()

    results = data["results"]

    context = {
        'results': results
    }

    return render(request, 'pages/bussness.html', context)


def blogsene(request):

    newsblog = blog.objects.all()
    context = {

        "newsblog": newsblog
    }
    return render(request, 'pages/blogs.html', context)


def blogdetail(request, title: str):
    try:
        newsblog = blog.objects.get(title=title)

    except blog.DoesNotExist:
        raise ("le poste n'excite pas")
    return render(request, "pages/blog_detail.html", {"newsblog": newsblog})


def newsdetail(request, title: str):
    try:
        data = results.objects.get(title=title)

    except blog.DoesNotExist:
        raise ("le poste n'excite pas")
    return render(request, "pages/news_detail.html", {"newsblog": newsblog})


# Create your views here.

# views.py

# views.py

# newsapp/views.py
