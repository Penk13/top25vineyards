from django.db import models
from vineyards.models import Vineyard


class WineRegion(models.Model):
    name = models.CharField(max_length=255)
    vineyards = models.ManyToManyField(Vineyard, blank=True, related_name="wineregion_filter")

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=255)
    wine_rg = models.ManyToManyField(WineRegion, blank=True)

    def __str__(self):
        wine_region_list = ""
        for i in self.wine_rg.all():
            wine_region_list += i.name + ", "
        if wine_region_list == "":
            return self.name
        else:
            return self.name + " - " + wine_region_list[0:-2]


class GeoRegion(models.Model):
    name = models.CharField(max_length=255)
    country = models.ManyToManyField(Country, blank=True)

    def __str__(self):
        return self.name


class WorldArea(models.Model):
    name = models.CharField(max_length=255)
    geo_region = models.ManyToManyField(GeoRegion, blank=True)

    def __str__(self):
        return self.name


class Wine(models.Model):
    name = models.CharField(max_length=255)
    vineyards = models.ManyToManyField(Vineyard, blank=True, related_name="wine_filter")

    def __str__(self):
        return self.name


class Facility(models.Model):
    name = models.CharField(max_length=255)
    vineyards = models.ManyToManyField(Vineyard, blank=True, related_name="facility_filter")

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=255)
    vineyards = models.ManyToManyField(Vineyard, blank=True, related_name="service_filter")

    def __str__(self):
        return self.name


class Rating(models.Model):
    name = models.CharField(max_length=255)
    vineyards = models.ManyToManyField(Vineyard, blank=True, related_name="rating_filter")

    def __str__(self):
        return self.name
