from django.contrib import admin
from .models import Product, Category

admin.site.site_header = 'Ecommerce'
admin.site.site_title = "ECommerce Admin Area"
admin.site.index_title = "Welcome to ECommerce admin area"

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_image','title', 'price', 'category')
    list_filter = ('category',)
    def product_image(self,obj):
        return obj.image_preview()
    product_image.short_description = 'Product image preview'
    product_image.allow_tags = True




admin.site.register(Category)