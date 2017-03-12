from django.contrib import admin
from django.contrib.contenttypes.admin import GenericInlineModelAdmin

from likes.models import Like


class LikeInline(admin.StackedInline, GenericInlineModelAdmin):

    model = Like
    ct_field = 'target_content_type'
    ct_fk_field = 'target_id'
