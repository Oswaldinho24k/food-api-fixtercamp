from django.shortcuts import render
from rest_framework import viewsets
from .models import Dish, Restaurant
from .serializers import DishSerializer, RestaurantSerializer
from rest_framework.permissions import IsAuthenticated

class DishViewSet(viewsets.ModelViewSet):
	queryset = Dish.objects.all()
	serializer_class = DishSerializer
	permission_classes = [IsAuthenticated]

class RestaurantViewSet(viewsets.ModelViewSet):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantSerializer
	permission_classes = [IsAuthenticated]
