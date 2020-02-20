from django.contrib import admin
from django.contrib import auth

from .models import Recipe, Ingredient, Info


class IngredientInline(admin.StackedInline):
    model = Ingredient
    extra = 1
    min_num = 1


class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredientInline, ]


admin.site.register(Recipe, RecipeAdmin)

admin.site.register(Info)
