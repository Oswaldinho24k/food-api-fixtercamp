from django.urls import path, include
from rest_framework import routers
from .views import DishViewSet, RestaurantViewSet
from accounts.views import UserViewSet

app_name="dishes"

router = routers.DefaultRouter()
router.register('dishes', DishViewSet)
router.register('restaurants', RestaurantViewSet)
router.register('users', UserViewSet)


urlpatterns=[
	path('', include(router.urls)),
]