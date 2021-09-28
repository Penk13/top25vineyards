from django.db import models
from ckeditor.fields import RichTextField
from django.db.models.signals import pre_save
from django.utils.text import slugify


class Region(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = RichTextField()
    sidebar = RichTextField(blank=True)
    ad_manager = models.TextField(blank=True)
    meta_keywords = models.TextField(blank=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return "Region : " + self.name


def create_slug_region(instance, new_slug=None):
    slug = slugify(instance.name)
    if new_slug is not None:
        slug = new_slug
    qs = Region.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug_region(instance, new_slug=new_slug)
    return slug


def pre_save_receiver_region(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug_region(instance)


pre_save.connect(pre_save_receiver_region, sender=Region)


class RegionChild(models.Model):
    name = models.CharField(max_length=255)
    region_parent = models.ForeignKey(Region, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return "Region : " + self.name + self.region_parent.name


def create_slug_region_child(instance, new_slug=None):
    slug = slugify(instance.name)
    if new_slug is not None:
        slug = new_slug
    qs = RegionChild.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug_region_child(instance, new_slug=new_slug)
    return slug


def pre_save_receiver_region_child(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug_region_child(instance)


pre_save.connect(pre_save_receiver_region_child, sender=RegionChild)


class RegionImage(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    region_images = models.ImageField(upload_to="region-image/")


class Vineyard(models.Model):
    name = models.CharField(max_length=255)
    text = RichTextField()
    rating = models.FloatField()
    google_map = models.TextField()
    wine_rg_url = models.URLField(blank=True)
    wine_rg = models.CharField(max_length=255)
    wines_url = models.URLField(blank=True)
    wines = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    grapes = models.CharField(max_length=255)
    owner_url = models.URLField(blank=True)
    owner = models.CharField(max_length=255)
    visits = models.CharField(max_length=255)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    cover = models.ImageField(upload_to="vineyard/")
    sidebar = RichTextField(blank=True)
    ad_manager = models.TextField(blank=True)
    meta_keywords = models.TextField(blank=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return "Vineyard : " + self.name


def create_slug_vineyard(instance, new_slug=None):
    slug = slugify(instance.name)
    if new_slug is not None:
        slug = new_slug
    qs = Vineyard.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug_vineyard(instance, new_slug=new_slug)
    return slug


def pre_save_receiver_vineyard(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug_vineyard(instance)


pre_save.connect(pre_save_receiver_vineyard, sender=Vineyard)
