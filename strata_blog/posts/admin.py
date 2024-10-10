from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'short_description',
        'content',
        'img',
        'created_at',
        'author',
    )
    search_fields = ('name', 'created_at', )
    list_filter = ('name', 'created_at', )
    readonly_fields = ('created_at', )
