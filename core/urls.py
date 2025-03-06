from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.products.urls')),
    path('api_user/', include('apps.users.urls')),
    path('api_order/', include('apps.orders.urls')),
    path('api_cart/', include('apps.carts.urls')),
    path('api_category/', include('apps.categories.urls')),
    path('', include('rest_framework.urls')),
]

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
