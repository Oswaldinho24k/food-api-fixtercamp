from django.db import models

# Create your models here.

class Dish(models.Model):

	nombre = models.CharField(max_length=140)
	precio = models.DecimalField(decimal_places=2, max_digits=10)
	descripcion = models.TextField()
	foto = models.ImageField(upload_to='dish_photos', blank=True, null=True)

	def __str__(self):
		return self.nombre
