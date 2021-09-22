from django.contrib import admin
from .models import RegionImage, Region, RegionChild, Vineyard


class RegionImageInline(admin.TabularInline):
    model = RegionImage


class RegionAdmin(admin.ModelAdmin):
    inlines = [RegionImageInline]


admin.site.register(Region, RegionAdmin)
admin.site.register(RegionChild)
admin.site.register(Vineyard)
