from django.shortcuts import render, get_object_or_404
from .models import Product
# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def product_detail(request, product_name):
    product = get_object_or_404(Product, name=product_name)
    return render(request, 'products/product_detail.html', {'product': product})
