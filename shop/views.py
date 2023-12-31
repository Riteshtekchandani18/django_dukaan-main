from django.shortcuts import render
from .models import Product,Brand,Category
from .filters import ProductFilter
from  django.contrib import messages

def all_products(request):
    f = ProductFilter(request.GET, queryset=Product.objects.all())
    return render(request,'shop/products.html',{
        'filter':f,
        'brands':Brand.objects.filter(favorite=True),
        'categories':Category.objects.all()
    })

def brandproduct(request,brand):
     brandObj = Brand.objects.get(slug=brand)
     products=Product.objects.filter(brand=brandObj)
     return render(request,'shop/brandproduct.html',{
        'brand': brandObj,
        'products': products,
        'brands': Brand.objects.all(),
        'categories': Category.objects.all()
    })

def category_products(request,category):
     catObj = Category.objects.get(slug=category)
     products=Product.objects.filter(category=catObj)
     return render(request,'shop/category_products.html',{
        'category': catObj,
        'products': products,
        'brands': Brand.objects.all(),
        'categories': Category.objects.all()
        })
def search_products(request):
     q = request.GET.get('q')
     if q is None:
          messages.error(request, 'Please enter something to search!')
     product_list_1 = Product.objects.filter(name__icontains=q)
     product_list_2 = Product.objects.filter(brand__name__icontains =q)
     product_list_3 = Product.objects.filter(category__name__icontains =q)
     return render(request,'shop/search.html',{
        'products': product_list_1.union(product_list_2,product_list_3),
        'brands': Brand.objects.filter(name__icontains=q),
        'categories':Category.objects.filter(name__icontains=q),
        'q':q,
        'total_items': product_list_1.count() + product_list_2.count() + product_list_3.count()
     })
  