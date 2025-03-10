from rest_framework import serializers

from django.contrib.auth import get_user_model



User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'photo', 'bio']


class SignUpSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'password', 'photo', 'bio']

    def create(self, validated_data):
        password = validated_data['password']
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user            