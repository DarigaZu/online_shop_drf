from rest_framework import serializers

from apps.orders.models import Order, Address, PaymentMethod


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ['id', 'street', 'city', 'zip_code']


class PaymentMethodSerializer(serializers.ModelSerializer):

    class Meta:
        model = PaymentMethod
        fields = ['id', 'method']


class OrderSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    payment_method = PaymentMethodSerializer()

    class Meta:
        model = Order
        fields = ['id', 'user', 'address', 'payment_method' 'created_at', 'updated_at', 'status']

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        payment_data = validated_data.pop('payment_method')
        address = Address.objects.create(**address_data)
        payment_method = PaymentMethod.objects.create(**payment_data)
        order = Order.objects.create(address=address, payment_method=payment_method, **validated_data)
        return order