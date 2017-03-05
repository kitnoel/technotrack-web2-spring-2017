# coding: utf8

from __future__ import unicode_literals
from core.models import Authored, Dated, Eventable, Request, User
from django.db import models


class FriendRequest(Dated, Eventable, Request):

    def accept(self):
        pass

    template_name = 'friend_request'

    def get_event_title(self):
        return '{} wants to be your friend.'. format(self.author)

    def __unicode__(self):
        return u'From {} To {}'.format(str(self.author), str(self.to_user))


class Friendship(Authored):
    to_user = models.ForeignKey(User, related_name='receiver')

    def __unicode__(self):
        return u'Between {} and {}'.format(str(self.author), str(self.to_user))
