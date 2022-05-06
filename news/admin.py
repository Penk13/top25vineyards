from django.contrib import admin
from .models import Category, Tag, Post, Autoblogging, Billboard, Article


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)
    search_fields = ['title', 'body']
    list_filter = ('category',)


class BillboardAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_filter = ('display',)


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Autoblogging)
admin.site.register(Post, PostAdmin)
admin.site.register(Billboard, BillboardAdmin)
admin.site.register(Article)
