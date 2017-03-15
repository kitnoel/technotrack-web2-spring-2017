from django.db.models.signals import post_save, post_delete, pre_save

from feed.models import Event
from relationships.models import Friendship, FriendRequest


def check_request(instance, *args, **kwargs):

    instance.accepted_old = instance.accepted


def change_friendship(instance, created=False, *args, **kwargs):
    if instance.accepted_old != instance.accepted:
        if not instance.accepted:
            for fr in instance.friendships:
                fr.delete()
        else:
            Friendship.objects.create(from_user=instance.author, to_user=instance.to_user).save()
            Friendship.objects.create(from_user=instance.to_user, to_user=instance.author).save()
    instance.save()

pre_save.connect(check_request, sender=FriendRequest)
post_save.connect(change_friendship, sender=FriendRequest)
