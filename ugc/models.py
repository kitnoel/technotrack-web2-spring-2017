from __future__ import unicode_literals
from django.db import models

from core.models import Authored, Dated
from feed.models import Eventable
from likes.models import Likeable


class Post(Authored, Dated, Eventable, Likeable):

    content = models.TextField(max_length=500)
    # template_name = 'post_template'
    #

    class Meta:
        ordering = ('-created',)

    # @models.permalink
    # def get_absolute_url(self):

    def get_event_title(self):
        return '{} published new post "{}"'.format(self.author, self.content[:32])

    def get_feed_state(self):
        return self.content.__hash__()

    def __unicode__(self):
        return u'{}'.format(self.content[:32])


class Comment(Authored, Dated, Eventable, Likeable):
    text = models.CharField(max_length=255)
    post = models.ForeignKey('Post', related_name='comments')
    ordering = ('-created',)
    # template_name = 'comment_template'

    def get_event_title(self):
        return '{} commented post "{}"'.format(self.author)

    def get_feed_state(self):
        return self.text.__hash__()

    def __unicode__(self):
        return u'{}'.format(self.text)
