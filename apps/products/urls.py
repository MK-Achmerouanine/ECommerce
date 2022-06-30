from django.urls import path
from .views import add_product, product_list, product_details

app_name = "products"

urlpatterns = [
    path('products/add/', add_product, name="add_product"),
    path('products/', product_list, name="product_list"),
    path('products/<id>/', product_details, name="product_details"),
]
