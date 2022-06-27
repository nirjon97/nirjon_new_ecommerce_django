from django.contrib import admin
from .models import Category,Product,Comment,CommenttForm

# Register your models here.
admin.site.register(Category)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'created_at', 'updated_at', 'image_tag']
    list_filter = ['title', 'created_at']
    list_per_page = 10
    search_fields = ['title', 'new_price', 'detail']


admin.site.register(Product,ProductAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['product', 'status', 'created_at', 'updated_at', 'user']
    list_filter = ['status', 'created_at']
    list_per_page = 10


admin.site.register(Comment,CommentAdmin)