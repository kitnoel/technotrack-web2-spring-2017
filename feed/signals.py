import hashlib

from django.db.models.signals import post_save, post_delete, pre_save

from feed.models import Eventable, Event


def check_state(instance, *args, **kwargs):

    instance.state_old = instance.get_feed_state()


def create_event(instance, created=False, *args, **kwargs):

    if created:
        e = Event.objects.create(object=instance, type='created')

    elif instance.state_old != instance.get_feed_state():
        e = Event.objects.create(object=instance, type='updated')

for eventable in Eventable.__subclasses__():
    pre_save.connect(check_state, sender=eventable)
    post_save.connect(create_event, sender=eventable)