from django.db import models
from ckeditor.fields import RichTextField
from django.db.models.signals import pre_save
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return "Category " + self.name


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return "Tag " + self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextField()
    tags = models.ManyToManyField(Tag)
    cover = models.ImageField(upload_to="news/", max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, max_length=200)

    def __str__(self):
        return "Post : " + self.title


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
