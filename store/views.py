from django.shortcuts import render
from django.http import HttpRequest, request
from .models import Product
def store(request):
    products = Product.objects.all().filter(is_available = True)
    context = {
        'products': products,
    }
    return render(request, 'home.html', context=context)