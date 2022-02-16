from django.contrib import admin
from .models import ContentPage, ImageUpload, Navbar, Footer, Sidebar


class ImageUploadInline(admin.TabularInline):
    model = ImageUpload


class ContentPageAdmin(admin.ModelAdmin):
    inlines = [ImageUploadInline]
    search_fields = ['title', 'content']


admin.site.register(ContentPage, ContentPageAdmin)
admin.site.register(Navbar)
admin.site.register(Footer)
admin.site.register(Sidebar)
