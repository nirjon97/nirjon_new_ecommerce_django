from django.contrib import admin

# Register your models here.
from UserApp.models import UserProfile,wishlist_cart



class UserProfileAdmin(admin.ModelAdmin):
	list_display=['user','country','image_tag']
	list_filter=['user',]

admin.site.register(UserProfile,UserProfileAdmin)

class wishlistAdmin(admin.ModelAdmin):
	list_display = ['user', 'product', 'price',]
    


admin.site.register(wishlist_cart,wishlistAdmin)