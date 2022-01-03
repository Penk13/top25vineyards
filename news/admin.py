from django.contrib import admin
from .models import Category, Tag, Post, Autoblogging, Billboard


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)
    search_fields = ['title', 'body']


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag)
admin.site.register(Autoblogging)
admin.site.register(Post, PostAdmin)
admin.site.register(Billboard)
