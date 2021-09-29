from django.contrib import admin
from .models import RegionImage, Region, RegionChild, Vineyard, YardImage, YardCoverImage


class RegionImageInline(admin.TabularInline):
    model = RegionImage


class RegionAdmin(admin.ModelAdmin):
    inlines = [RegionImageInline]
    readonly_fields = ('slug',)


class RegionChildAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)


class YardImageInline(admin.TabularInline):
    model = YardImage


class YardCoverImageInline(admin.TabularInline):
    model = YardCoverImage


class VineyardAdmin(admin.ModelAdmin):
    inlines = [YardImageInline, YardCoverImageInline]
    readonly_fields = ('slug',)


admin.site.register(Region, RegionAdmin)
admin.site.register(RegionChild, RegionChildAdmin)
admin.site.register(Vineyard, VineyardAdmin)
