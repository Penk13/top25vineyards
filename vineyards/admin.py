from django.contrib import admin
from .models import RegionImage, Region, RegionChild, Vineyard


class RegionImageInline(admin.TabularInline):
    model = RegionImage


class RegionAdmin(admin.ModelAdmin):
    inlines = [RegionImageInline]
    readonly_fields = ('slug',)


class RegionChildAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)


class VineyardAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)


admin.site.register(Region, RegionAdmin)
admin.site.register(RegionChild, RegionChildAdmin)
admin.site.register(Vineyard, VineyardAdmin)
