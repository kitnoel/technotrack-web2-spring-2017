# coding: utf8
from __future__ import unicode_literals

from django.db import models
from django.db.models import ForeignKey

from core.models import Authored, Dated, User
from feed.models import Eventable


class Request(Authored):  # friend, invite etc
    accepted = models.BooleanField(default=False)
    to_user = models.ForeignKey(User, related_name='to_user')

    def accept(self):
        raise NotImplementedError

    class Meta:
        abstract = True


class FriendRequest(Dated, Eventable, Request):

    def accept(self):
        pass

    # template_name = 'friend_request'
    #
    def get_event_title(self):
        return '{} wants to be friend of {}'. format(self.author, self.to_user)

    def get_feed_state(self):
        return self.accepted

    def __unicode__(self):
        return u'From {} To {}'.format(str(self.author), str(self.to_user))


class Friendship(models.Model):
    request = models.ForeignKey(FriendRequest, related_name='friendships')
    from_user = models.ForeignKey(User, related_name='sender')
    to_user = models.ForeignKey(User, related_name='receiver')

    def __unicode__(self):
        return u'Between {} and {}'.format(str(self.author), str(self.to_user))
