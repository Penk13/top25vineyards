from django.contrib import admin
from .models import RegionImage, Region, Vineyard, TopSliderImage, CoverSliderImage, ReviewAndRating


class RegionImageInline(admin.TabularInline):
    model = RegionImage


class RegionAdmin(admin.ModelAdmin):
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


class ReviewAndRatingAdmin(admin.ModelAdmin):
    search_fields = ['title', 'review']


admin.site.register(Region, RegionAdmin)
admin.site.register(Vineyard, VineyardAdmin)
admin.site.register(ReviewAndRating, ReviewAndRatingAdmin)
