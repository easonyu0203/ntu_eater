from django.shortcuts import render
from django.http import HttpResponse
from .models import Restaurant, RestaurantImage
from .serializers import RestaurantSerialer, RestaurantImageSerialer
from rest_framework import generics, viewsets


class RestaurantViewSet(viewsets.ModelViewSet):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantSerialer


class RestaurantImageViewSet(viewsets.ModelViewSet):
	queryset = RestaurantImage.objects.all()
	serializer_class = RestaurantImageSerialer

