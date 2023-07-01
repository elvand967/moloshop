# D:\Python\django\elvand\moloshop\blog\urls.py


from django.urls import path, re_path

from blog.views import *

urlpatterns = [
    path('', index),
    # path('cats/<int:catid>/', categories),
    path('cats/<slug:cat>/', categories),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),
]
