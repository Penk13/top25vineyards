from django.db import models
from ckeditor.fields import RichTextField

TYPE = (
    ("PAGE", "Page"),
    ("HOME_PAGE", "Home Page"),
    ("HOME_PAGE_SIDEBAR", "Home Page Sidebar")
)


class ContentPage(models.Model):
    types = models.CharField(max_length=20, choices=TYPE)
    title = models.CharField(max_length=255)
    content = RichTextField(blank=True)

    def __str__(self):
        return self.get_types_display() + " : " + self.title
