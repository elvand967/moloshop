# D:\Python\django\elvand\moloshop\blog\templatetags\blog_tags.py

from django import template
from blog.models import *


register = template.Library()


@register.simple_tag(name='getcats')  # simple_tag - экземпляр класса Library()
def get_categories(filter=None):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(slug=filter)


@register.inclusion_tag('blog/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)

    return {"cats": cats, "cat_selected": cat_selected}

