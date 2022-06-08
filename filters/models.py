from django.db import models
from vineyards.models import Vineyard


class WineRegion(models.Model):
    name = models.CharField(max_length=255)
    vineyards = models.ManyToManyField(Vineyard, blank=True, related_name="wineregion_filter")

    def __str__(self):
        return self.name

    def get_world_region_id(self):
        return WorldRegion.objects.get(country=Country.objects.get(wine_rg=self)).id

    def get_country_id(self):
        return Country.objects.get(wine_rg=self).id


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

    def get_wine_region_id(self):
        result = list(self.wine_rg.values_list('id', flat=True))
        final_result = ','.join(str(num) for num in result)
        return final_result

    def get_world_region_id(self):
        return WorldRegion.objects.get(country=self).id


class WorldRegion(models.Model):
    name = models.CharField(max_length=255)
    country = models.ManyToManyField(Country, blank=True)
    order = models.IntegerField(unique=True)

    def __str__(self):
        return self.name

    def get_country_id(self):
        result = list(self.country.values_list('id', flat=True))
        final_result = ','.join(str(num) for num in result)
        return final_result

    def get_wine_region_id(self):
        wine_region_list = []
        for country in self.country.all():
            for wine_region in country.wine_rg.all():
                wine_region_list.append(wine_region.id)
        result = list(dict.fromkeys(wine_region_list))
        final_result = ','.join(str(num) for num in result)
        return final_result


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
    order = models.IntegerField(unique=True)

    def __str__(self):
        return self.name
