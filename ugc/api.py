from rest_framework import serializers, viewsets, permissions
from .models import Post
from application.api import router
from core.api import UserSerializer


class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'content', 'author', 'created', 'updated', 'likes_count']


# class PostingPermission(permissions.BasePermission):
#
#     def has_object_permission(self, request, view, obj):
#         return obj.author == request.author


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        qs = super(PostViewSet, self).get_queryset()
        if self.request.query_params.get('author'):
            qs = qs.filter(author_id=self.request.query_params.get('author'))
        return qs

router.register('posts', PostViewSet)
