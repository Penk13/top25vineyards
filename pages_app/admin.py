from django.contrib import admin
from .models import ContentPage


class ContentPageAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)


admin.site.register(ContentPage, ContentPageAdmin)
