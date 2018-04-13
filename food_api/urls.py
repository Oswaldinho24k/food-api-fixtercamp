from django.contrib import admin
from django.urls import path, include

from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from dishes import urls as dishes_urls
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(dishes_urls, namespace="dishes")),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', views.obtain_auth_token),
     url(
        regex=r'^media/(?P<path>.*)$',
        view=serve,
        kwargs={'document_root': settings.MEDIA_ROOT}
    ),
]
