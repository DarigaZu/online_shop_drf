from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from apps.categories.models import Category, SubCategory
from apps.categories.serializers import CategorySerializer, SubCategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]


class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer    