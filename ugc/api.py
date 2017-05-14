from rest_framework import serializers, generics, viewsets, permissions
from .models import Post
from application.api import router
from core.api import UserSerializer


class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Post
        fields = 'content', 'author',


# class PostRetriever(generics.RetrieveAPIView):
#
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

class MyPermission(permissions.BasePermission):

    # readed by any users, written only by author
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user


class PostViewSet(viewsets.ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = permissions.IsAuthenticated, MyPermission,

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):  # GET /api/posts/?author=1
        qs = super(PostViewSet, self).get_queryset()
        # qs = filter(author=self.request.user)
        if 'author' in self.request.query_params:
            qs = qs.filter(author=self.request.query_params['author'])
        return qs

router.register('posts', PostViewSet)  # prefix of urls