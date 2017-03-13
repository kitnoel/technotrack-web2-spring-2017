from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.template import Template


class User(AbstractUser):

    pass


class Authored(models.Model):
    author = models.ForeignKey(User)

    class Meta:
        abstract = True


class Dated(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Request(Authored):  # friend, invite etc
    accepted = models.BooleanField(default=False)
    to_user = models.ForeignKey(User, related_name='to_user')

    def accept(self):
        raise NotImplementedError

    class Meta:
        abstract = True



