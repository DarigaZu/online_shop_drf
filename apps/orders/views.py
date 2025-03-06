from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth import get_user_model

from apps.orders.models import Order
from apps.orders import serializers


User = get_user_model()


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = serializers.OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)