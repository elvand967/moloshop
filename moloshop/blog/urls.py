# D:\Python\django\elvand\moloshop\blog\urls.py


from django.urls import path, re_path

from blog.views import *




urlpatterns = [
    path('', BlogHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', BlogCategory.as_view(), name='category'),
]
