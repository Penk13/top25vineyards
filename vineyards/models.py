from django.db import models
from ckeditor.fields import RichTextField


class Region(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = RichTextField()

    def __str__(self):
        return "Region : " + self.name


class RegionChild(models.Model):
    name = models.CharField(max_length=255)
    region_parent = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return "Region : " + self.name + self.region_parent.name


class RegionImage(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    region_images = models.ImageField(upload_to="region-image/")


class Vineyard(models.Model):
    name = models.CharField(max_length=255)
    text = RichTextField()
    rating = models.FloatField()
    google_map = models.TextField()
    size = models.CharField(max_length=255)
    grapes = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)
    visits = models.CharField(max_length=255)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    cover = models.ImageField(upload_to="vineyard/")

    def __str__(self):
        return "Vineyard : " + self.name
