from django.contrib import admin
from .models import Recipe, Ingredient

# admin.site.register(Recipe)


class IngredientInline(admin.StackedInline):
    model = Ingredient
    extra = 1
    min_num = 1


class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredientInline, ]


admin.site.register(Recipe, RecipeAdmin)
