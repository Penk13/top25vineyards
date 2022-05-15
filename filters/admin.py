from django.contrib import admin
from .models import WineRegion, Country, GeoRegion, WorldArea


admin.site.register(WineRegion)
admin.site.register(Country)
admin.site.register(GeoRegion)
admin.site.register(WorldArea)
