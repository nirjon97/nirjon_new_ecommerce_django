from django.urls import path
from .views import Comment_Add


urlpatterns = [
    path('comment/<int:id>/' , Comment_Add , name="Comment_Add"),

    ]