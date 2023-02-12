from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from diana.views import *
from django.urls import path, include

from djsite import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('diana.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = pageNotFound