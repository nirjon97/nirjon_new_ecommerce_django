from django.urls import path
from OrderApp.views import Add_to_Shoping_cart,cart_detials,cart_delete,OrderCart,cart_update,user_order_details

urlpatterns = [
    path('addingcart/<int:id>/', Add_to_Shoping_cart, name='Add_to_Shoping_cart'),
    path('cart/', cart_detials, name= 'cart_detials'),
    path('cart_delete/<int:id>/', cart_delete, name='cart_delete'),
    path('oder_cart/', OrderCart, name='OrderCart'),
    path('cart_update/<int:id>/', cart_update, name='cart_update'),
    path('order_details/<int:id>/', user_order_details, name='user_order_details'),
   

]
