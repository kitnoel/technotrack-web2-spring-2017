from django.db.models import Q
from rest_framework import serializers, viewsets, permissions

from .models import Message, Chat

from application.api import router
from core.api import UserSerializer, UserViewSet


class MessageSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Message
        fields = ['content', 'chat', 'author', 'created', 'id']


# class IsInChat(permissions.BasePermission):
#
#     def has_object_permission(self, request, view, obj):
#         if obj.__class__ == Message:
#             return request.user in obj.chat.users.all()
#         elif obj.__class__ == Chat:
#             return request.user in obj.users.all()
#         else:
#             raise permissions.exceptions.MethodNotAllowed()


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get_queryset(self):
        qs = super(MessageViewSet, self).get_queryset()
        qs = qs.filter(
            Q(author=self.request.user) |
            Q(chat__users=self.request.user)
        )
        qs = qs.distinct()
        chat = self.request.query_params.get('chat')
        if chat is not None:
            qs = qs.filter(chat=chat)
        return qs

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ChatSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    last_message = serializers.SerializerMethodField()

    def get_last_message(self, obj):
        try:
            return MessageSerializer(obj.messages.latest('created')).data
        except:
            return None

    class Meta:
        model = Chat
        fields = ['id', 'users', 'last_message', 'author', 'title']


class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

    def get_queryset(self):
        qs = super(ChatViewSet, self).get_queryset()
        qs = qs.filter(
            Q(author=self.request.user) |
            Q(users=self.request.user)
        )
        qs = qs.distinct()
        return qs

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

router.register('messages', MessageViewSet)
router.register('chats', ChatViewSet)
