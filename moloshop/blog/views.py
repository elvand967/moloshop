# D:\Python\django\elvand\moloshop\blog\views.py

from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


def index(request):
    return HttpResponse("Страница приложения blog.")  # http://127.0.0.1:8000/blog/


# def categories(request, catid):
#     return HttpResponse(f"<h1>Статьи по категориям</h1>{catid}</p>")

def categories(request, cat):
    if (request.GET):
        print(request.GET)

    return HttpResponse(f"<h1>Статьи по категориям</h1>{cat}</p>")


def archive(request, year):
    if (int(year) > 2023):
        raise Http404()
    elif (int(year) > 2020):
        return redirect('/')

    return HttpResponse(f"<h1>Архив по годам</h1>{year}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')