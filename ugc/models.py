from __future__ import unicode_literals
from core.models import Authored, Dated, Eventable
from django.db import models


class Post(Authored, Dated, Eventable):
    content = models.TextField(max_length=500)
    template_name = 'post'

    def get_event_title(self):
        return '{} published new post "{}"'.format(self.author, self.content[:32])

    def __unicode__(self):
        return u'{}'.format(self.content[:32])


class Comment(Authored, Dated, Eventable):
    text = models.CharField(max_length=255)
    post = models.ForeignKey('Post', related_name='comments')
    ordering = ('-created',)
    template_name = 'comment'

    def get_event_title(self):
        return '{} commented post "{}"'.format(self.author)

    def __unicode__(self):
        return u'{}'.format(self.text)
