from django.shortcuts import render
from rest_framework import viewsets
from .models import Dish, Restaurant
from .serializers import DishSerializer, RestaurantSerializer

class DishViewSet(viewsets.ModelViewSet):
	queryset = Dish.objects.all()
	serializer_class = DishSerializer

class RestaurantViewSet(viewsets.ModelViewSet):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantSerializer
