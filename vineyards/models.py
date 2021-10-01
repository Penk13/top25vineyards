from django.db import models
from ckeditor.fields import RichTextField
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.urls import reverse


class Region(models.Model):
    region_parent = models.ForeignKey(
        "self", blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = RichTextField()
    sidebar = RichTextField(blank=True)
    ad_manager = models.TextField(blank=True)
    meta_keywords = models.TextField(blank=True)
    logo_on_navbar = models.ImageField(
        upload_to="logo-on-navbar/", blank=True, max_length=255)
    display_on_navbar = models.BooleanField(default=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        try:
            return "Region : " + self.name + ', Parent : ' + self.region_parent.name
        except:
            return "Region : " + self.name

    def get_absolute_url(self):
        return reverse('vineyards:region', kwargs={'slug': self.slug})


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


class RegionImage(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    region_images = models.ImageField(
        upload_to="region-image/", max_length=255)


class Vineyard(models.Model):
    name = models.CharField(max_length=255)
    text = RichTextField()
    rating = models.FloatField()
    custom_overlay = models.ImageField(
        upload_to="custom-rating/", blank=True, max_length=255)
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
    regions = models.ManyToManyField(
        Region, blank=True, related_name="regions")
    cover = models.ImageField(upload_to="vineyard/", max_length=255)
    sidebar = RichTextField(blank=True)
    ad_manager = models.TextField(blank=True)
    meta_keywords = models.TextField(blank=True)
    top_slider = models.BooleanField(default=False)
    cover_slider = models.BooleanField(default=False)
    hide_rating = models.BooleanField(default=False)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return "Vineyard : " + self.name

    def get_absolute_url(self):
        if self.region.region_parent is not None:
            return reverse('vineyards:detail', kwargs={'parent': self.region.region_parent.slug, 'region': self.region.slug, 'slug': self.slug})
        else:
            return reverse('vineyards:detail-without-parent', kwargs={'region': self.region.slug, 'slug': self.slug})


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


class TopSliderImage(models.Model):
    vineyard = models.ForeignKey(Vineyard, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="yard-image/", max_length=255)


class CoverSliderImage(models.Model):
    vineyard = models.ForeignKey(Vineyard, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="yard-cover-image/", max_length=255)
