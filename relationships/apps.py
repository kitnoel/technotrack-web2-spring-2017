from __future__ import unicode_literals

from django.apps import AppConfig


class RelationshipsConfig(AppConfig):
    name = 'relationships'

    def ready(self):

        import signals