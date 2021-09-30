from django.contrib import admin
from .models import ContentPage, ImageUpload


class ImageUploadInline(admin.TabularInline):
    model = ImageUpload


class ContentPageAdmin(admin.ModelAdmin):
    inlines = [ImageUploadInline]
    readonly_fields = ('slug',)


admin.site.register(ContentPage, ContentPageAdmin)
