from rest_framework import serializers

from apps.carts.models import Cart, CartItem
from apps.products.serializers import ProductSerializer


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = ['id', 'cart', 'product', 'quantity']

    def create(self, validated_data):
        request = self.context.get('request')
        cart = Cart.objects.get(user=request.user)  # Получаем корзину текущего пользователя
        validated_data['cart'] = cart  # Устанавливаем корзину
        return super().create(validated_data)



class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items']