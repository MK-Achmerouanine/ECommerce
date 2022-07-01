from xml.etree.ElementInclude import include
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from .views import home
from django.conf.urls.static import static
from django.conf import settings
from .views import login_page, logout_page
app_name = "core"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('login/', login_page),
    path('logout/', logout_page, name="logout"),
    path('products/', include('apps.products.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)