# D:\Python\django\elvand\moloshop\blog\views.py
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.forms import forms
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from .forms import AddPostForm, RegisterUserForm, LoginUserForm
from .models import *

from django.views.generic import ListView, DetailView, CreateView
from .utils import *

from django.contrib.auth.mixins import LoginRequiredMixin

class BlogHome(DataMixin, ListView):
    # paginate_by = 2
    model = Blog
    template_name = 'blog/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        return Blog.objects.filter(is_published=True)


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'blog/addpage.html'
    # login_url = reverse_lazy('home')
    raise_exception = True
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление статьи")
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class ShowPost(DataMixin, DetailView):
    model = Blog
    template_name = 'blog/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))


class BlogCategory(DataMixin, ListView):
    model = Blog
    template_name = 'blog/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Blog.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Категория - ' + str(context['posts'][0].cat),
                                      cat_selected=context['posts'][0].cat_id)
        return dict(list(context.items()) + list(c_def.items()))


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'blog/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    # form_class = AuthenticationForm
    form_class = LoginUserForm
    template_name = 'blog/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    '''
    Этот же эффект можно получить, определив константу
    LOGIN_REDIRECT_URL = '/'
    в файле settings.py пакета конфигурации ...\moloshop\settings.py.
    '''
    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


# @login_required              # теперь страница доступна только для зарегистрированных/авторезированных пользователей
def about(request):
    contact_list = Blog.objects.all()
    paginator = Paginator(contact_list, 2)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/about.html', {'page_obj': page_obj, 'menu': menu, 'title': 'О сайте'})


def contact(request):
    return HttpResponse("<h1>Обратная связь</h1>")


# def login(request):
#     return HttpResponse("<h1>Авторизация</h1>")


def archive(request, year):
    if (int(year) > 2023):
        raise Http404()
    elif (int(year) > 2020):
        return redirect('/')

    return HttpResponse(f"<h1>Архив по годам</h1>{year}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')




