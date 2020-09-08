from django.contrib import admin

from posts.models import Post


@admin.register(Post)
class Post(admin.ModelAdmin):
    list_display = ('content', 'posted', 'created_at')
    readonly_fields = ('created_at',)
