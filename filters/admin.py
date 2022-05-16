from django.contrib import admin
from .models import WineRegion, Country, GeoRegion, WorldArea, Wine, Facility, Service


admin.site.register(WineRegion)
admin.site.register(Country)
admin.site.register(GeoRegion)
admin.site.register(WorldArea)
admin.site.register(Wine)
admin.site.register(Facility)
admin.site.register(Service)
