from __future__ import unicode_literals

from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

from core.models import Authored
from feed.models import Eventable


class Like(Authored, Eventable):

    def get_feed_state(self):
        pass

    def get_event_title(self):
        return '{} likes {} {}'.join(self.author, str(self.target_content_type), unicode(self.target))

    target_content_type = models.ForeignKey(ContentType)
    target_id = models.PositiveIntegerField()
    target = GenericForeignKey(ct_field='target_content_type', fk_field='target_id')


class Likeable(models.Model):
    likes = GenericRelation(
        Like,
        content_type_field='target_content_type',
        object_id_field='target_id',
    )

    likes_count = models.IntegerField(default=0)

    class Meta:
        abstract = True


