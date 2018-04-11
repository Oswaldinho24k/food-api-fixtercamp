from rest_framework import serializers
from .models import Dish, Restaurant, Ingrediente

class BasicDishSerializer(serializers.ModelSerializer):
	class Meta:
		model = Dish
		fields = ['id', 'nombre', 'foto', 'precio']

class BasicRestaurantSerializer(serializers.ModelSerializer):
	class Meta:
		model = Restaurant
		fields = '__all__'



class IngredienteSerializer(serializers.ModelSerializer):
	class Meta:
		model = Ingrediente
		fields = '__all__'

class RestaurantSerializer(serializers.ModelSerializer):
	dishes = BasicDishSerializer(many=True, read_only=True)
	class Meta:
		model = Restaurant
		fields = '__all__'

class DishSerializer(serializers.ModelSerializer):
	restaurant = BasicRestaurantSerializer(read_only=True, many=False)
	restaurant_id = serializers.PrimaryKeyRelatedField(
		queryset=Restaurant.objects.all(),
		write_only=True,
		required=False
		)
	ingredients = IngredienteSerializer(read_only=True, many=True)
	ingredients_id = serializers.PrimaryKeyRelatedField(
		queryset=Ingrediente.objects.all(),
		write_only=True,
		many=True
		)
	class Meta:
		model = Dish
		fields = '__all__'


	def create(self, validated_data):
		res = validated_data.pop('restaurant_id')
		ingredients = validated_data.pop('ingredients_id')
		dish = Dish.objects.create(restaurant=res, **validated_data)
		for ing in ingredients:
			dish.ingredients.add(ing)
		return dish








