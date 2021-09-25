from django.contrib import admin
from .models import Category, Tag, Post


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
