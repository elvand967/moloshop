# D:\Python\django\elvand\moloshop\blog\views.py

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Страница приложения blog.")  # http://127.0.0.1:8000/blog/


# def categories(request, catid):
#     return HttpResponse(f"<h1>Статьи по категориям</h1>{catid}</p>")

def categories(request, cat):
    return HttpResponse(f"<h1>Статьи по категориям</h1>{cat}</p>")


def archive(request, year):
    return HttpResponse(f"<h1>Архив по годам</h1>{year}</p>")