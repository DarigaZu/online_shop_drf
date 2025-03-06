from rest_framework.routers import DefaultRouter

from django.urls import path, include

from apps.users import views


router = DefaultRouter()
router.register('user', views.UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls))
]