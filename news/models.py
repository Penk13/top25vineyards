from django.db import models
from ckeditor.fields import RichTextField


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
    cover = models.ImageField(upload_to="news/")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return "Post : " + self.title
