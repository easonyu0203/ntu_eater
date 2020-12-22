from rest_framework import serializers
from .models import Restaurant

class RestaurantsSerialer(serializers.ModelSerializer):
	class Meta:
		model = Restaurant
		fields = ('name', 'location', 'phone_number')