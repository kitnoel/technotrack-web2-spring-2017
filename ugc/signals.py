from django.db.models.signals import post_delete, pre_delete

from likes.models import Likeable
from ugc.models import Post, Comment


def delete_related_content(instance, *args, **kwargs):
    if issubclass(instance.__class__, Likeable):
        for like in instance.likes.all():
            like.delete()

    if issubclass(instance.__class__, Post):
        for comment in instance.comments.all():
            comment.delete()
    instance.save()

pre_delete.connect(delete_related_content, sender=Post)
pre_delete.connect(delete_related_content, sender=Comment)
