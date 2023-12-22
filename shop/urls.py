from django.urls import path
from .import views

urlpatterns = [
 #listing of products
    path('products/all/', views.all_products, name='all_products'),
    path('products/<slug:brands>/all/',views.brand_products,name='brand_products'),
    path('products/<slug:category>/all/',views.category_products,name='category_products'),
    path('products/<slug:brands>/<slug:category>/all/',views.brands_category_products,name='brand_category_products'),

    #seaching products
    path('products/search/',views.search_products, name='search_products'),
]