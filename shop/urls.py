from django.urls import path
from . import views

urlpatterns = [
 #listing of products
    path('products/all/', views.all_products, name='all_products'),
    path('brands/<slug:brand>/all/',views.brandproduct,name='brandproduct'),
    path('category/<slug:category>/all/',views.category_products,name='category_products'),
   

    #seaching products
    path('products/search/',views.search_products, name='search_products'),
]