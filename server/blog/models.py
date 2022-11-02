from django.db import models
import uuid
from datetime import datetime
from category.models import Category


def blog_directory(instance, filename):
    return f'blog/{instance.title}/{filename}'


class Blog(models.Model):
    class BlogObject(models.Manager):
        def get_queryset(self):
            return super().get_queryset()
    options = (
        ('d', 'Draft'),
        ('p', 'Published')
    )
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    title = models.CharField(max_length=255, null=True)
    content = models.TextField(null=True)
    # image = models.ImageField(upload_to=blog_directory, blank=True, null=True)
    # author=models.CharField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    published = models.DateTimeField(default=datetime.now)
    status = models.CharField(max_length=1, choices=options, default='d')

    objects = models.Manager()
    blogobject = BlogObject()

    class Meta:
        ordering = ['-published']

    def __str__(self):
        return self.title

    # def get_image(self):
    #     if self.image.url:
    #         return self.image.url
    #     return ''
