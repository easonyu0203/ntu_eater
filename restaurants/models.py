from django.db import models



# Create your models here.
class Restaurant(models.Model):

	name = models.CharField(max_length=200)
	location = models.CharField(max_length=200)
	phone_number = models.CharField(max_length=100)
	intro = models.CharField(max_length=1000, default='')
	main_img = models.ForeignKey( 'RestaurantImage', blank=True, null=True, on_delete=models.DO_NOTHING, related_name='main_img')

	def __str__(self):
		return f'{self.name}'


class RestaurantImage(models.Model):
	image = models.ImageField(upload_to='restaurantImage')
	restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE, related_name='RestaurantImages')

