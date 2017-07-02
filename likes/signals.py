from celery import shared_task
from django.db.models.signals import post_save, post_delete, pre_delete

from likes.models import Like


@shared_task
def set_likes_count(like_id):
    instance = Like.objects.get(id=like_id)
    instance.target.likes_count = instance.target.likes.count()
    instance.target.save()


def add_like(instance, async=False, created=False, *args, **kwargs):
    if async:
        set_likes_count.apply_async([instance.id])
    else:
        instance.target.likes_count = instance.target.likes.count()
        instance.target.save()


def delete_like(instance, *args, **kwargs):
    instance.target.likes_count = instance.target.likes.count() - 1
    instance.target.save()


post_save.connect(add_like, sender=Like)

pre_delete.connect(delete_like, sender=Like)
