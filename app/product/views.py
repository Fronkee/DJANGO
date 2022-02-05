from itertools import product
from django.shortcuts import render
from .models import Product
# Create your views here.
def allProducts(request):
    data = {
        'products'  : Product.objects.all(),
        'title'  : 'Products'
    }
    return render(request,'product/index.html',data) 

def cartView(request,item):
    orderList = item.split(',')
    products = Product.objects.filter(pk__in=orderList)
    return render(request,'product/cartview.html',{'products':products})