from django.db import models


class Image (models.Model):
    name = models.CharField(max_length=255, default='')
    pic = models.ImageField(
        default='gallery/brown_bottle.jpg', upload_to='gallery')

    def __str__(self):
        return self.name


class Recipe (models.Model):
    title = models.CharField(max_length=255, default='')
    description = models.TextField(default='', blank=True)
    instructions = models.TextField(default='', blank=True)
    tags = models.TextField(default='')
    image = models.ForeignKey(
        Image, default=1, on_delete=models.SET_DEFAULT, related_name='recipe_pic', blank=True, null=True)

    def __str__(self):
        return self.title


class Info(models.Model):
    name = models.CharField(max_length=255, default='')
    data = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} {self.data}"


class Ingredient(models.Model):
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name='ingredients')
    name = models.CharField(max_length=255, default='')
    measure = models.CharField(max_length=100, default='')
    info_link = models.ForeignKey(
        Info, on_delete=models.CASCADE, related_name='info', blank=True, null=True)

    def __str__(self):
        return f"{self.measure} {self.name}"


class Instructional(models.Model):
    title = models.CharField(max_length=255, default='')
    instructions = models.TextField(default='', blank=True)
    image = models.ForeignKey(
        Image, on_delete=models.SET_NULL, related_name='image', blank=True, null=True)

    def __str__(self):
        return self.title
