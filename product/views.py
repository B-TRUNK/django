from django.shortcuts import render
from .models import Product

# Create your views here.

def products(request):

    #product table all rows
    products = Product.objects.all()
    #query set
    pro = {'pro' :products.order_by('price')}
    return render(request, 'product/products.html' ,pro)

def product(request):
    return render(request, 'product/product.html')

