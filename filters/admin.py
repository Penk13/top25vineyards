from django.contrib import admin
from .models import WineRegion, Country, GeoRegion, WorldArea, Wine, Facility, Service
from vineyards.models import Vineyard
from django.db.models import Q
from django.db.models.functions import Lower


class WineRegionAdmin(admin.ModelAdmin):
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        try:
            wine_rg_id = request.resolver_match.kwargs["object_id"]
            wine_rg = WineRegion.objects.get(id=wine_rg_id)
            if db_field.name == "vineyards":
                kwargs["queryset"] = Vineyard.objects.filter(Q(region__name__contains=wine_rg.name) | Q(regions__name__contains=wine_rg.name)).distinct()
        except:
            pass
        return super(WineRegionAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)
    filter_horizontal = ('vineyards',)
    search_fields = ['name']


class WineAdmin(admin.ModelAdmin):
    filter_horizontal = ('vineyards',)


class FacilityAdmin(admin.ModelAdmin):
    filter_horizontal = ('vineyards',)


class ServiceAdmin(admin.ModelAdmin):
    filter_horizontal = ('vineyards',)


admin.site.register(WineRegion, WineRegionAdmin)
admin.site.register(Country)
admin.site.register(GeoRegion)
admin.site.register(WorldArea)
admin.site.register(Wine, WineAdmin)
admin.site.register(Facility, FacilityAdmin)
admin.site.register(Service, ServiceAdmin)
