from __future__ import unicode_literals
from core.models import Authored, Dated, User
from django.db import models

# Create your models here.


class Chat(Authored, Dated):
    title = models.CharField(max_length=64)
    users = models.ManyToManyField(User, related_name='chats')

    class Meta:
        ordering = ('-created',)


    def __unicode__(self):
        return u'{}'.format(self.title[:32])


class Message(Authored, Dated):
    chat = models.ForeignKey(Chat, related_name='messages')
    content = models.CharField(max_length=200)

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'{}'.format(self.content[:32])