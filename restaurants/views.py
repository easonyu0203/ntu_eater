from django.shortcuts import render
from django.http import HttpResponse
from .models import Restaurant
from .serializers import RestaurantsSerialer
from rest_framework import generics


class RestaurantListCreate(generics.ListCreateAPIView):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantsSerialer

class RestaurantRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantsSerialer
