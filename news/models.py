from django.db import models
from ckeditor.fields import RichTextField
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=200, blank=True)

    def __str__(self):
        return "Category " + self.name


def create_slug_category(instance, new_slug=None):
    slug = slugify(instance.name)
    if new_slug is not None:
        slug = new_slug
    qs = Category.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug_category(instance, new_slug=new_slug)
    return slug


def pre_save_receiver_region(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug_category(instance)


pre_save.connect(pre_save_receiver_region, sender=Category)


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return "Tag " + self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextField()
    tags = models.ManyToManyField(Tag, blank=True)
    cover = models.ImageField(
        upload_to="news", blank=True, max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sidebar = RichTextField(blank=True)
    ad_manager = models.TextField(blank=True)
    meta_description = models.TextField(blank=True)
    meta_keywords = models.TextField(blank=True)
    slug = models.SlugField(unique=True, max_length=200)

    def __str__(self):
        return "Post : " + self.title

    def get_absolute_url(self):
        return reverse('news:detail', kwargs={'category': self.category.slug, 'news': self.slug})


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


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
    image = models.ImageField(upload_to="billboard", max_length=255)
    url = models.URLField(max_length=255)

    def __str__(self):
        return self.title
