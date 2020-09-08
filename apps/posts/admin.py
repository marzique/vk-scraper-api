from django.contrib import admin
from rest_framework.authtoken.admin import TokenAdmin

from posts.models import Post


@admin.register(Post)
class Post(admin.ModelAdmin):
    list_display = ('snippet', 'posted', 'created_at')
    readonly_fields = ('created_at',)
    list_display_links = list_display

    def snippet(self, obj):
        return obj.content[:10] 


TokenAdmin.raw_id_fields = ['user']