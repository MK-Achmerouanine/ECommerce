from unicodedata import category
from django.shortcuts import render

from apps.products.models import Product, Category

def home(request):
    cat = Category.objects.filter(title = 'Clothes').first()
    ctx = {
        "products": Product.objects.filter(category=cat)
    }
    return render(request, 'home.html', ctx)