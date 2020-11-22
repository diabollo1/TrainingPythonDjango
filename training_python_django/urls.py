from django.conf import settings
from django.contrib import admin
from django.urls import path
from cake.views import *
from website.views import *
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('category/<category_id>', category, name='category'),
    path('cake/<product_id>', product, name='cake'),
    path('website', website, name='website'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
