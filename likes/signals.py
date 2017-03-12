from django.db.models.signals import post_save

from likes.models import Like


def recount_likes_for_post(instance, *args, **kwargs):

    pass

post_save.connect(recount_likes_for_post, sender=Like)
