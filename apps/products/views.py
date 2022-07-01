from django.shortcuts import redirect, render
from .forms import ProductForm
from .models import Product
from django.contrib.auth.decorators import login_required
from core.decorators import allowed_users
def product_list(request):
    prds = Product.objects.all()
    context = {
        'products': prds
    }
    return render(request, 'products/list.html', context)

@allowed_users(allowed_roles=['Test'])
def product_details(request, id):
    prd = Product.objects.filter(id=id).first()
    context = {
        'product': prd
    }
    return render(request, 'products/details.html', context)
"""
d = {
    "title": 'titre',
    "object": {
        "attrs": [1,2,3,4,5,6],
        'other': {'hack': 'it'}
    }
}
d['object']['other']['hack']
d.get('object').get('other').get('hack')
"""

@login_required(login_url="/login")
def add_product(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            print(request.POST)
            form.save()
            return redirect('products:product_list')
            """
            p = Product(
                title= request.POST.get('title'),
                price=request.POST['price']
            )
            """
        else:
            form = ProductForm(data=request.POST)
    context = {
        'form': form
    }
    return render(request, 'products/add.html', context)