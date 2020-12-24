from rest_framework import serializers
from .models import Restaurant, RestaurantImage

class RestaurantSerialer(serializers.ModelSerializer):
	class Meta:
		model = Restaurant
		fields = ('id', 'name', 'location', 'phone_number', 'intro', 'main_img')

class RestaurantImageSerialer(serializers.ModelSerializer):
	class Meta:
		model = RestaurantImage
		fields = ('id', 'image', 'restaurant') 
