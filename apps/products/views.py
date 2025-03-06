from rest_framework import viewsets

from apps.products.models import Product
from apps.products import serializers
from apps.products.permissions import IsAdminUserOrReadOnly


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)  
    
    def get_serializer_class(self):
        if self.action in ['create']:
            return serializers.ProductCreateSerializer
        return self.serializer_class
  