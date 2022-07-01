from django.urls import path
from .views import add_product, product_list, product_details

app_name = "products"

urlpatterns = [
    path('add/', add_product, name="add_product"),
    path('', product_list, name="product_list"),
    path('<id>/', product_details, name="product_details"),
]
