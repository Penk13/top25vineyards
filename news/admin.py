from django.contrib import admin
from .models import Category, Tag, Post, Autoblogging


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Autoblogging)
admin.site.register(Post, PostAdmin)
