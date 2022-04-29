from django.contrib import admin
from .models import RegionImage, Region, Vineyard, TopSliderImage, CoverSliderImage, ReviewAndRating, Comment
from import_export.admin import ImportExportModelAdmin
from .resources import VineyardResource


class RegionImageInline(admin.TabularInline):
    model = RegionImage


class RegionAdmin(admin.ModelAdmin):
    search_fields = ['name']
    inlines = [RegionImageInline]
    readonly_fields = ('slug', 'id',)


class TopSliderImageInline(admin.TabularInline):
    model = TopSliderImage


class CoverSliderImageInline(admin.TabularInline):
    model = CoverSliderImage


class VineyardAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    inlines = [TopSliderImageInline, CoverSliderImageInline]
    readonly_fields = ('id', 'add_date', 'mod_date')
    search_fields = ['name', 'text']
    list_filter = ['display','region']
    list_display = ('id', 'name', 'add_date', 'mod_date', 'isvalidated',)
    list_display_links = ('id', 'name')
    resource_class = VineyardResource


class ReviewAndRatingAdmin(admin.ModelAdmin):
    search_fields = ['title', 'review']
    list_filter = ['approved']


class CommentAdmin(admin.ModelAdmin):
    search_fields = ['title', 'body']
    list_filter = ['approved']


admin.site.register(Region, RegionAdmin)
admin.site.register(Vineyard, VineyardAdmin)
admin.site.register(ReviewAndRating, ReviewAndRatingAdmin)
admin.site.register(Comment, CommentAdmin)
