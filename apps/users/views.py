from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from django.contrib.auth import get_user_model

from apps.users import serializers



User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action in ['create']:
            return serializers.SignUpSerializer
        return self.serializer_class

    def get_queryset(self):
        return User.objects.none() 

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)