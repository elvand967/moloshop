# D:\Python\django\elvand\moloshop\moloshop\urls.py
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from blog.views import *
from moloshop import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]


# процес необходим для работы в отладочном режиме
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = pageNotFound

