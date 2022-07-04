from django.contrib import admin
from .models import WineRegion, Country, WorldRegion, Wine, Facility, Service, Rating
from vineyards.models import Vineyard


class WineRegionAdmin(admin.ModelAdmin):
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        try:
            obj_id = request.resolver_match.kwargs["object_id"]
            obj = WineRegion.objects.get(id=obj_id)
            if db_field.name == "vineyards":
                kwargs["queryset"] = Vineyard.objects.filter(filter_tags__icontains=obj.name).distinct()
        except:
            pass
        return super(WineRegionAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)
    filter_horizontal = ('vineyards',)
    search_fields = ['name']


class WineAdmin(admin.ModelAdmin):
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        try:
            obj_id = request.resolver_match.kwargs["object_id"]
            obj = Wine.objects.get(id=obj_id)
            if db_field.name == "vineyards":
                kwargs["queryset"] = Vineyard.objects.filter(filter_tags__icontains=obj.name).distinct()
        except:
            pass
        return super(WineAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)
    filter_horizontal = ('vineyards',)


class FacilityAdmin(admin.ModelAdmin):
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        try:
            obj_id = request.resolver_match.kwargs["object_id"]
            obj = Facility.objects.get(id=obj_id)
            if db_field.name == "vineyards":
                kwargs["queryset"] = Vineyard.objects.filter(filter_tags__icontains=obj.name).distinct()
        except:
            pass
        return super(FacilityAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)
    filter_horizontal = ('vineyards',)


class ServiceAdmin(admin.ModelAdmin):
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        try:
            obj_id = request.resolver_match.kwargs["object_id"]
            obj = Service.objects.get(id=obj_id)
            if db_field.name == "vineyards":
                kwargs["queryset"] = Vineyard.objects.filter(filter_tags__icontains=obj.name).distinct()
        except:
            pass
        return super(ServiceAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)
    filter_horizontal = ('vineyards',)


class RatingAdmin(admin.ModelAdmin):
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        try:
            obj_id = request.resolver_match.kwargs["object_id"]
            obj = Rating.objects.get(id=obj_id)
            if db_field.name == "vineyards":
                kwargs["queryset"] = Vineyard.objects.filter(filter_tags__icontains=obj.name).distinct()
        except:
            pass
        return super(RatingAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)
    filter_horizontal = ('vineyards',)


admin.site.register(WineRegion, WineRegionAdmin)
admin.site.register(Country)
admin.site.register(WorldRegion)
admin.site.register(Wine, WineAdmin)
admin.site.register(Facility, FacilityAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Rating, RatingAdmin)
