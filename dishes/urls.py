from django.urls import path, include
from rest_framework import routers
from .views import DishViewSet

app_name="dishes"

router = routers.DefaultRouter()
router.register('dishes', DishViewSet)

urlpatterns=[
	path('', include(router.urls)),
]