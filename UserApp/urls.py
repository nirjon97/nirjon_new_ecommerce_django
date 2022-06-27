from django.urls import path
from .views import user_logout,user_login,user_register,userprofile,user_update,user_password,add_to_user_wishlist,wishlist_detials,wishlist_delete
urlpatterns = [

    path('logout/', user_logout, name= 'user_logout'),
    path('login/', user_login , name='user_login' ),
    path('register/', user_register , name='user_register' ),
    path('profile/', userprofile , name='userprofile' ),
    path('user_update/', user_update, name="user_update"),
    path('password_update/', user_password, name="user_password"),
    path('adding_wishlist/<int:id>/', add_to_user_wishlist, name="add_to_user_wishlist"),
    path('wishlist/', wishlist_detials, name= 'wishlist_detials'),
    path('wishlist_delete/<int:id>/', wishlist_delete, name='wishlist_delete'),


    ]