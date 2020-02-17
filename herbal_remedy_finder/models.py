from django.db import models


class Recipe (models.Model):
    title = models.CharField(max_length=255, default='')
    description = models.TextField(default='')
    ingredients = models.TextField(default='')
    instructions = models.TextField(default='')
    pic = models.ImageField(blank=True)

    def __str__(self):
        return self.title
