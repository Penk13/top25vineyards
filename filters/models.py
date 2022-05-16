from django.db import models
from vineyards.models import Vineyard


class WineRegion(models.Model):
    name = models.CharField(max_length=255)
    vineyards = models.ManyToManyField(Vineyard, blank=True)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=255)
    wine_rg = models.ManyToManyField(WineRegion, blank=True)

    def __str__(self):
        return self.name


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
    vineyards = models.ManyToManyField(Vineyard, blank=True)

    def __str__(self):
        return self.name


class Facility(models.Model):
    name = models.CharField(max_length=255)
    vineyards = models.ManyToManyField(Vineyard, blank=True)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=255)
    vineyards = models.ManyToManyField(Vineyard, blank=True)

    def __str__(self):
        return self.name
