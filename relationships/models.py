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

    # template_name = 'friend_request'
    #
    prev_state = models.BooleanField(default=False)

    def accept(self):
        if self.friendships.count() == 0:
            self.accepted = True
            self.save(force_update=True)

    def reject(self):
        if self.friendships.count() > 0:
            self.prev_state = self.accepted
            self.accepted = False
            self.save(force_update=True)

    def get_event_title(self):
        return '{} wants to be friend of {}'. format(self.author, self.to_user)

    def get_feed_state(self):
        return self.prev_state

    def __unicode__(self):
        return u'From {} To {}'.format(str(self.author), str(self.to_user))


class Friendship(models.Model):
    request = models.ForeignKey(FriendRequest, related_name='friendships')
    from_user = models.ForeignKey(User, related_name='sender')
    to_user = models.ForeignKey(User, related_name='receiver')

    def __unicode__(self):
        return u'Between {} and {}'.format(str(self.author), str(self.to_user))
