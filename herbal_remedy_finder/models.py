from django.db import models


class Recipe (models.Model):
    title = models.CharField(max_length=255, default='')
    description = models.TextField(default='')
    instructions = models.TextField(default='')
    pic = models.ImageField(blank=True)
    tags = models.TextField(default='')

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name='ingredients')
    name = models.CharField(max_length=255, default='')
    measure = models.CharField(max_length=100, default='')
    info = models.TextField(blank=True)

    def __str__(self):
        return f"{self.measure} {self.name}"
