from rest_framework import serializers, viewsets, permissions
from .models import Post
from application.api import router
from core.api import UserSerializer


class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ['content', 'likes_count', 'author', 'created', 'updated', 'id', ]
        read_only_fields = ['likes_count', 'author', 'created', 'updated', 'id', ]


class IsAuthor(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request._request.method in ('GET', ):
            return True
        else:
            return obj.author == request.user


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthor, ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        qs = super(PostViewSet, self).get_queryset()
        if self.request.query_params.get('author'):
            qs = qs.filter(author_id=self.request.query_params.get('author'))
        return qs

router.register('posts', PostViewSet)
