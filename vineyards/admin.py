from re import search
from django.contrib import admin
from .models import RegionImage, Region, Vineyard, VineyardUser, TopSliderImage, CoverSliderImage, ReviewAndRating


class RegionImageInline(admin.TabularInline):
    model = RegionImage


class RegionAdmin(admin.ModelAdmin):
    search_fields = ['name']
    inlines = [RegionImageInline]
    readonly_fields = ('slug',)


class TopSliderImageInline(admin.TabularInline):
    model = TopSliderImage


class CoverSliderImageInline(admin.TabularInline):
    model = CoverSliderImage


class VineyardAdmin(admin.ModelAdmin):
    inlines = [TopSliderImageInline, CoverSliderImageInline]
    readonly_fields = ('slug',)
    search_fields = ['name', 'text']
    list_filter = ['region', 'display']


class VineyardUserAdmin(admin.ModelAdmin):
    search_fields = ('vineyard__name', 'name',)


class ReviewAndRatingAdmin(admin.ModelAdmin):
    search_fields = ['title', 'review']
    list_filter = ['approved']


admin.site.register(Region, RegionAdmin)
admin.site.register(Vineyard, VineyardAdmin)
admin.site.register(VineyardUser, VineyardUserAdmin)
admin.site.register(ReviewAndRating, ReviewAndRatingAdmin)
