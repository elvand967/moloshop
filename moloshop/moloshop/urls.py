# D:\Python\django\elvand\moloshop\moloshop\urls.py


from django.contrib import admin
from django.urls import path, include

from blog.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]

handler404 = pageNotFound