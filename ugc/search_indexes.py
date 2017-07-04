import datetime
from haystack import indexes
from .models import Post


class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    author = indexes.CharField(model_attr='author')
    created = indexes.DateTimeField(model_attr='created')

    autocomplete = indexes.EdgeNgramField()

    def get_model(self):
        return Post

    # @staticmethod
    # def prepare_autocomplete(obj):
    #     return " ".join((
    #         obj.author, obj.created
    #     ))

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(created__lte=datetime.datetime.now())