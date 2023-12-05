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

    results = data["results"]

    context = {
        'results': results
    }

    return render(request, 'pages/index.html', context)


def politique(request):
    url = f'https://newsdata.io/api/1/news?country=sn&apikey=pub_33467774e35656a9e0c14a93978036b649c82'
    response = requests.get(url)
    # Raise an exception for bad responses (4xx and 5xx status codes)
    response.raise_for_status()
    data = response.json()

    results = data["results"]

    context = {
        'results': results
    }

    return render(request, 'pages/politique.html', context)

# Create your views here.

# views.py

# views.py

# newsapp/views.py
