from django.db.models.signals import post_save, post_delete

from likes.models import Like


def add_like(instance, created=False, *args, **kwargs):
    if created:
        instance.target.likes_count = instance.target.likes.count()
    instance.target.save()


def delete_like(instance, *args, **kwargs):
    instance.target.likes_count = instance.target.likes.count()
    instance.target.save()


post_save.connect(add_like, sender=Like)

post_delete.connect(delete_like, sender=Like)
