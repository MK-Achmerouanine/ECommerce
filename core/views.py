from django.shortcuts import render

def home(request):
    ctx = {}
    return render(request, 'home.html', ctx)