from django.urls import path, include

from rest_framework.routers import DefaultRouter

from apps.products import views


router = DefaultRouter()
router.register('product', views.ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls))
]