from django.urls import path
from restaurants.views import RestaurantListCreate, RestaurantRetrieveUpdateDestroy

urlpatterns = [
	path('restaurant/', RestaurantListCreate.as_view()),
	path('restaurant/<int:pk>', RestaurantRetrieveUpdateDestroy.as_view())
]