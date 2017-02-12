from __future__ import unicode_literals
from core.models import Authored, Dated, Eventable
from django.db import models


class Post(Authored, Dated, Eventable):
    post_id = models.IntegerField()
    content = models.CharField(max_length=500)
    template_name = 'post'

    def get_event_title(self):
        return '{} published new post "{}"'.format(self.author, self.content[:32])

    def __unicode__(self):
        return u'{}'.format(self.content[:32])
