import random
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.urls import reverse
from filer.fields.image import FilerImageField

import vineyards.models


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=200, blank=True)

    def __str__(self):
        return "Category " + self.name


def pre_save_receiver_category(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)


pre_save.connect(pre_save_receiver_category, sender=Category)


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return "Tag " + self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextUploadingField()
    tags = models.ManyToManyField(Tag, blank=True)
    cover = models.ImageField(
        upload_to="news", blank=True, max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    sidebar = models.TextField(blank=True)
    ad_manager = models.TextField(blank=True)
    meta_description = models.TextField(blank=True)
    meta_keywords = models.TextField(blank=True)
    display_news = models.BooleanField(default=True)
    display_billboard = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, max_length=200)

    def __str__(self):
        return "Post : " + self.title

    def get_absolute_url(self):
        return reverse('news-detail', kwargs={'category': self.category.slug, 'news': self.slug})


def create_slug_post(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    pt = Post.objects.filter(slug=slug)
    rg = vineyards.models.Region.objects.filter(slug=slug)
    if pt.exists() or rg.exists():
        new_slug = "%s-%s" % (slug, str(random.randrange(1, 1000, 1)))
        return create_slug_post(instance, new_slug=new_slug)
    return slug


def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug_post(instance)


pre_save.connect(pre_save_receiver, sender=Post)


class Autoblogging(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    items = models.IntegerField(default=15)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Billboard(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="billboard", blank=True, max_length=255)
    image2 = FilerImageField(null=True, blank=True, on_delete=models.CASCADE)
    url = models.URLField(max_length=255)
    display = models.BooleanField(default=True)

    def __str__(self):
        return self.title
