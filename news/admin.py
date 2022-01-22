from django.contrib import admin
from .models import Category, Tag, Post, Autoblogging, Billboard


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)
    search_fields = ['title', 'body']


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Autoblogging)
admin.site.register(Post, PostAdmin)
admin.site.register(Billboard)
