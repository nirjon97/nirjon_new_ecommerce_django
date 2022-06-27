from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('nirjon712764/', admin.site.urls),
    path('', include('base_app.urls')),
    path('user/', include('UserApp.urls')),
    path('product/', include('Product.urls')),
    path('order/', include('OrderApp.urls')),
] 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)