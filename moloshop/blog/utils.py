# D:\Python\django\elvand\moloshop\blog\utils.py

from django.db.models import Count

from .models import *
# from django.core.cache import cache

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
]


class DataMixin:
    paginate_by = 2
    def get_user_context(self, **kwargs):
        context = kwargs
        # ------- API кэширование
        # cats = cache.get('cats')
        # if not cats:
        #     cats = Category.objects.annotate(Count('blog'))
        #     cache.set('cats', cats, 60)
        # -------
        # cats = Category.objects.all()
        # -------
        cats = Category.objects.annotate(Count('blog'))

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)  # если пользователь не авторизован, из списка меню удаляем 2-ой элемент (1)

        context['menu'] = user_menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0

        return context