from django.shortcuts import render

from apps.products.models import Product

def product_list(request):
    prds = Product.objects.all()
    context = {
        'products': prds
    }
    return render(request, 'products/list.html', context)