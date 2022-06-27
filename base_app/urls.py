from django.urls import path,include
from .views import Home,gender_category,men_category,women_category,category_product,product_details,newsletter,contact,search_view
from django.views.generic import TemplateView
#from .views import HomeView

urlpatterns = [
      #function based view
      path('product/',include('Product.urls')),
      path('', Home, name='Home'),
      path('contact/', contact, name='contact'),
      path('newsletter/', newsletter, name='newsletter'),
      path('search/', search_view, name='search_view'),
      path('gender_category/', gender_category, name='gender_category'),
      path('men_category/', men_category, name='men_category'),
      path('women_category/', women_category, name='women_category'),
      path('category_product/<str:slug>', category_product, name='category_product'),
      path('product_details/<str:cate_slug>/<int:id>/',product_details, name='product_details'),
      

      #class based view
      #path('',HomeView.as_view()),
       
]