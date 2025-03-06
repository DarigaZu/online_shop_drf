from rest_framework.routers import DefaultRouter

from django.urls import path, include

from apps.orders import views


router = DefaultRouter()
router.register('order', views.OrderViewSet, basename='order')

urlpatterns = [
    path('', include(router.urls))
]