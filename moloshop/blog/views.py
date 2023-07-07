# D:\Python\django\elvand\moloshop\blog\views.py

from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'},
]


def index(request):
    posts = Blog.objects.all()
    # cats = Category.objects.all()

    context = {
        'posts': posts,
        # 'cats': cats,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0,
    }

    return render(request, 'blog/index.html', context=context)


def about(request):
    return render(request, 'blog/about.html', {'menu': menu, 'title': 'О сайте'})


def addpage(request):
    return HttpResponse("<h1>Добавление статьи</h1>")


def contact(request):
    return HttpResponse("<h1>Обратная связь</h1>")


def login(request):
    return HttpResponse("<h1>Авторизация</h1>")


def categories(request, cat):
    if (request.GET):
        print(request.GET)

    return HttpResponse(f"<h1>Статьи по категориям {cat}</h1>")


def show_category(request, cat_id):
    posts = Blog.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id,
    }

    return render(request, 'blog/index.html', context=context)


def archive(request, year):
    if (int(year) > 2023):
        raise Http404()
    elif (int(year) > 2020):
        return redirect('/')

    return HttpResponse(f"<h1>Архив по годам</h1>{year}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def show_post(request, post_slug):
    post = get_object_or_404(Blog, slug=post_slug)
    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': 1,
    }
    return render(request, 'blog/post.html', context=context)


