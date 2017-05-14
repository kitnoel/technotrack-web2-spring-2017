from __future__ import unicode_literals

from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models

from core.models import Authored


class Event(Authored):
    type = models.CharField(max_length=64)  # one from ['created', 'updated']
    object_content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    object = GenericForeignKey(ct_field='object_content_type', fk_field='object_id')


class Eventable(models.Model):
    # template_name = None
    #
    # def get_event_html(self):
    #     return Template('events/{}_html.html'.format(self.template_name), {'object': self})
    #
    def get_event_title(self):
        raise NotImplementedError

    def get_feed_state(self):
        raise NotImplementedError

    events = GenericRelation(
        Event,
        content_type_field='object_content_type',
        object_id_field='object_id'
    )

    class Meta:
        abstract = True

