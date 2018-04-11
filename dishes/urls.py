from django.urls import path, include
from rest_framework import routers
from .views import DishViewSet, RestaurantViewSet

app_name="dishes"

router = routers.DefaultRouter()
router.register('dishes', DishViewSet)
router.register('restaurants', RestaurantViewSet)

urlpatterns=[
	path('', include(router.urls)),
]