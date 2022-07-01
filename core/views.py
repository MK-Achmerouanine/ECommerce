from django.shortcuts import redirect, render

from apps.products.models import Product, Category
from django.contrib.auth import authenticate, login, logout
from .decorators import unauthenticated_user
from core.forms import LoginForm
def home(request):
    cat = Category.objects.filter(title = 'Clothes').first()
    ctx = {
        "products": Product.objects.filter(category=cat)
    }
    return render(request, 'home.html', ctx)

@unauthenticated_user
def login_page(request):
    form = LoginForm()
    ctx = {
        "form": form
    }
    if request.method == "POST":
        user = authenticate(username=request.POST.get('username'), password= request.POST.get('password'))
        if user is not None:
            # redirect to homepage
            login(request, user)
            return redirect('/')
    return render(request, 'login.html', ctx)

def logout_page(request):
    logout(request)
    return redirect('/')