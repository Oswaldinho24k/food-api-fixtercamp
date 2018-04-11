from django.db import models

# Create your models he

class Restaurant(models.Model):
	nombre = models.CharField(max_length=100)

	def __str__(self):
		return self.nombre

class Ingrediente(models.Model):
	nombre = models.CharField(max_length=100)

	def __str__(self):
		return self.nombre

class Dish(models.Model):

	nombre = models.CharField(max_length=140)
	precio = models.DecimalField(decimal_places=2, max_digits=10)
	descripcion = models.TextField()
	foto = models.ImageField(upload_to='dish_photos', blank=True, null=True)
	restaurant = models.ForeignKey(Restaurant, related_name='dishes', on_delete=models.CASCADE, blank=True, null=True)
	ingredients = models.ManyToManyField(Ingrediente, related_name='dishes')

	def __str__(self):
		return self.nombre





