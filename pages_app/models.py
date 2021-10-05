from django.db import models
from ckeditor.fields import RichTextField
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.urls import reverse
from vineyards.models import Region

TYPE = (
    ("PAGE", "Page"),
    ("FOOTER", "Footer"),
    ("HOME_PAGE", "Home Page"),
    ("SEARCH_PAGE", "Search Page")
)


class ContentPage(models.Model):
    types = models.CharField(max_length=20, choices=TYPE)
    title = models.CharField(max_length=255)
    content = RichTextField(blank=True)
    sidebar = RichTextField(blank=True)
    ad_manager = models.TextField(blank=True)
    meta_keywords = models.TextField(blank=True)
    additional_content = RichTextField(blank=True)
    category = models.ForeignKey(
        Region, null=True, blank=True, on_delete=models.CASCADE)
    show_listing = models.BooleanField(default=False)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.get_types_display() + " : " + self.title

    def get_absolute_url(self):
        if self.types == "HOME_PAGE":
            return reverse('pages_app:mainpage')
        elif self.types == "FOOTER":
            return reverse('pages_app:footerpage', kwargs={'slug': self.slug})
        elif self.types == "PAGE":
            return reverse('pages_app:page', kwargs={'slug': self.slug})


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = ContentPage.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_receiver, sender=ContentPage)


class ImageUpload(models.Model):
    page = models.ForeignKey(ContentPage, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="page/", max_length=255)


class Navbar(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField(blank=True)
    region = models.ManyToManyField(Region, blank=True)
    page = models.ManyToManyField(ContentPage, blank=True)
    order = models.IntegerField(unique=True)

    def __str__(self):
        return self.title
