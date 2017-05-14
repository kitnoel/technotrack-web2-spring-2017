from rest_framework import serializers, generics, viewsets, permissions
from .models import User
from application.api import router


class UserSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = 'username', 'event'


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

router.register('users', UserViewSet)