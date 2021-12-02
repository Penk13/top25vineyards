from django.contrib import admin
from .models import ContentPage, ImageUpload, Navbar


class ImageUploadInline(admin.TabularInline):
    model = ImageUpload


class ContentPageAdmin(admin.ModelAdmin):
    inlines = [ImageUploadInline]
    readonly_fields = ('slug',)
    search_fields = ['title', 'content']


admin.site.register(ContentPage, ContentPageAdmin)
admin.site.register(Navbar)
