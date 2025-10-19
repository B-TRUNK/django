from django.shortcuts import render
from .models import Product

# Create your views here.

def products(request):
    return render(request, 'product/products.html' ,{'pro' :Product.objects.all()})

def product(request):
    return render(request, 'product/product.html')