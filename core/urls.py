from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from .views import home
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('products/', include('apps.products.urls')),
]
