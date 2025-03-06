from rest_framework.routers import DefaultRouter
from django.urls import path, include

from apps.carts import views


router = DefaultRouter()
router.register('cart', views.CartViewSet, basename='cart')
router.register('cart_item', views.CartItemViewSet, basename='cart_item')

urlpatterns = [
    path('', include(router.urls))
]