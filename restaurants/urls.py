from django.urls import path, include
from rest_framework.routers import DefaultRouter
from restaurants.views import (
	RestaurantViewSet,
	RestaurantImageViewSet
	)

router = DefaultRouter()
router.register(r'restaurant', RestaurantViewSet)
router.register(r'restaurantImage', RestaurantImageViewSet)
 
urlpatterns = [
	path('', include(router.urls)),
]