from django.urls import path, include

from rest_framework.routers import DefaultRouter

from apps.categories import views


router = DefaultRouter()
router.register('categories', views.CategoryViewSet, basename='categories')
router.register('subcategories', views.SubCategoryViewSet, basename='subcategories')

urlpatterns = [
    path('', include(router.urls))
]