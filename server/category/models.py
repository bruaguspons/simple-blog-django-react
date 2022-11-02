from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, default='')
    image = models.ImageField(upload_to='media/category')

    def __str__(self):
        return self.name

    def get_image(self):
        return self.image.url if self.image.url else ''
