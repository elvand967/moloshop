# D:\Python\django\elvand\moloshop\blog\urls.py


from django.urls import path, re_path

from blog.views import *

urlpatterns = [
    # path('', index, name='home'),
    path('', BlogHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('addpage/', addpage, name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('post/<slug:post_slug>/', show_post, name='post'),
    # path('category/<int:cat_id>/', show_category, name='category'),
    path('category/<slug:cat_slug>/', BlogCategory.as_view(), name='category'),
]
