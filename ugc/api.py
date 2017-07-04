from rest_framework import serializers, viewsets, permissions

from ugc.search_indexes import PostIndex
from .models import Post
from application.api import router
from core.api import UserSerializer

from drf_haystack.serializers import HaystackSerializer
from drf_haystack.viewsets import HaystackViewSet


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


class PostSearchSerializer(HaystackSerializer):

    def to_representation(self, instance):
        return PostSerializer(instance.object).to_representation(instance.object)

    class Meta:
        # The `index_classes` attribute is a list of which search indexes
        # we want to include in the search.
        index_classes = [PostIndex]

        # The `fields` contains all the fields we want to include.
        # NOTE: Make sure you don't confuse these with model attributes. These
        # fields belong to the search index!
        fields = [
            "content"
        ]


class PostSearchView(HaystackViewSet):

    # `index_models` is an optional list of which models you would like to include
    # in the search result. You might have several models indexed, and this provides
    # a way to filter out those of no interest for this particular view.
    # (Translates to `SearchQuerySet().models(*index_models)` behind the scenes.
    # index_models = [Post]

    serializer_class = PostSearchSerializer

router.register('posts/search', PostSearchView, base_name='posts-search')
router.register('posts', PostViewSet)
