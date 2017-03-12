from django.contrib import admin

# Register your models here.
from likes.admin import LikeInline
from models import Post, Comment


class CommentInline(admin.TabularInline):
    model = Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    inlines = [CommentInline, LikeInline]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    pass
