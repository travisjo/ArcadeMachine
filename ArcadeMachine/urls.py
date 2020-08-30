from django.contrib import admin
from django.conf.urls import include
from django.urls import path

from api import urls as api_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urls)),
]
