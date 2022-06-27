from django.contrib import admin
from .models import Setting,ContactMessage,Newsletter

# Register your models here.
admin.site.register(Setting)
admin.site.register(ContactMessage)
admin.site.register(Newsletter)