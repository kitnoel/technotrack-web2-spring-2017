from rest_framework import serializers, viewsets, permissions, mixins
from .models import User
from application.api import router


class UserSettingsSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "is_active",
            "password",
        )
        read_only_fields = (
            "id",
            "is_active"
        )


class UserFullInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "is_active",
        )
        read_only_fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "is_active"
        )


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'id']


class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet,):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.suffix == u'List':
            return UserSerializer
        if self.get_object() == self.request.user:
            return UserSettingsSerializer
        else:
            return UserFullInfoSerializer

router.register('users', UserViewSet)
