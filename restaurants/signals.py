from django.db.models.signals import pre_delete, post_save
from django.dispatch import receiver
from .models import RestaurantImage

@receiver(pre_delete, sender=RestaurantImage)
def update_main_img_del(sender, **kwargs):
	rest_img = kwargs['instance']
	restaurant = rest_img.restaurant
	
	if restaurant.main_img == rest_img:
		img_list = [i for i in restaurant.RestaurantImages.all() if i != rest_img]
		restaurant.main_img = img_list[0]
		restaurant.save()		


@receiver(post_save, sender=RestaurantImage)
def update_main_img_sav(sender, **kwargs):
	rest_img = kwargs['instance']
	restaurant = rest_img.restaurant
	
	if restaurant.main_img is None:
		restaurant.main_img = rest_img
		restaurant.save()
