from django.contrib import admin
from django.urls import path, include

from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from dishes import urls as dishes_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(dishes_urls, namespace="dishes")),
     url(
        regex=r'^media/(?P<path>.*)$',
        view=serve,
        kwargs={'document_root': settings.MEDIA_ROOT}
    ),
]
