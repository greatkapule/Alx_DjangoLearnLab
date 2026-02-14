from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')
    list_filter = ('published_date',)
    date_hierarchy = 'published_date'


admin.site.register(Post, PostAdmin)
