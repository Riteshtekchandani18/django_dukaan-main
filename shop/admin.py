from django.contrib import admin

# Register your models here.
from .models import Category,Brand,Seller,Product,ProductImage,ProductReview

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    '''Admin View for Category'''

    list_display = ('name','slug')

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    '''Admin View for Brand'''

    list_display = ('name','slug','logo')

@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ('name','description')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','brand','seller','category','sprice','qty')

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product','image',)

@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ('product','user','review','rating')


