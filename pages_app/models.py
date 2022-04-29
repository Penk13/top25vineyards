from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.urls import reverse
from django.utils.html import strip_tags
import html
from vineyards.models import Region
from news.models import Category
from filer.fields.image import FilerImageField

TYPE = (
    ("PAGE", "Page"),
    ("FOOTER", "Footer"),
    ("HOME_PAGE", "Home Page"),
    ("SEARCH_PAGE", "Search Page"),
    ("CATEGORY", "Category"),
    ("WITHOUT_SIDEBAR", "Without Sidebar"),
)


class ContentPage(models.Model):
    types = models.CharField(max_length=20, choices=TYPE)
    thumbnail = models.ImageField(
        upload_to='thumbnail-page/', blank=True, max_length=255)
    thumbnail2 = FilerImageField(null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = RichTextUploadingField(blank=True)
    content_on_list = RichTextUploadingField(blank=True)
    sidebar = models.TextField(blank=True)
    ad_manager = models.TextField(blank=True)
    meta_description = models.TextField(blank=True)
    meta_keywords = models.TextField(blank=True)
    additional_content = RichTextUploadingField(blank=True)
    category = models.ManyToManyField(Region, blank=True)
    news = models.ManyToManyField(Category, blank=True)
    listing_title1 = models.CharField(max_length=255, blank=True)
    listing_title2 = models.CharField(max_length=255, blank=True)
    listing_title3 = models.CharField(max_length=255, blank=True)
    show_listing = models.BooleanField(default=False)
    display_news = models.BooleanField(default=True)
    display_billboard = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, blank=True, max_length=255)

    def __str__(self):
        return self.get_types_display() + " : " + self.title

    def get_absolute_url(self):
        if self.types == "HOME_PAGE":
            return reverse('pages_app:mainpage')
        elif self.types == "CATEGORY":
            return reverse('pages_app:newspage', kwargs={'slug': self.slug})
        elif self.types == "FOOTER":
            return reverse('pages_app:footerpage', kwargs={'slug': self.slug})
        elif self.types == "PAGE" or self.types == "WITHOUT_SIDEBAR":
            return reverse('pages_app:page', kwargs={'slug': self.slug})


def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)
    if not instance.meta_keywords:
        meta_key = instance.title.lower()
        instance.meta_keywords = meta_key
    if not instance.meta_description and instance.content:
        meta_desc = instance.content[0:instance.content.find(".")]
        instance.meta_description = html.unescape(strip_tags(meta_desc))


pre_save.connect(pre_save_receiver, sender=ContentPage)


class ImageUpload(models.Model):
    page = models.ForeignKey(ContentPage, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="page/", blank=True, max_length=255)
    image2 = FilerImageField(null=True, blank=True, on_delete=models.CASCADE)


class Navbar(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField(blank=True)
    region = models.ManyToManyField(Region, blank=True)
    page = models.ManyToManyField(ContentPage, blank=True)
    order = models.IntegerField(unique=True)

    def __str__(self):
        return self.title


class Footer(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField(blank=True)
    new_window = models.BooleanField(default=False)
    order = models.IntegerField(unique=True)

    def __str__(self):
        return self.title


class Sidebar(models.Model):
    sidebar = models.TextField(blank=True)
    ad_manager = models.TextField(blank=True)

    def __str__(self):
        return "Default Sidebar"


class Script(models.Model):
    name = models.CharField(max_length=255)
    script = models.TextField(blank=True)

    def __str__(self):
        return self.name
