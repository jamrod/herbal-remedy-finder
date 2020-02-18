from django import forms
from django.forms.models import inlineformset_factory
from django.forms.models import BaseInlineFormSet

from .models import Recipe, Ingredient


class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = ('title', 'description',
                  'instructions', 'pic', 'tags',)


class IngredientForm(forms.ModelForm):

    class Meta:
        model = Ingredient
        fields = ('recipe', 'measure', 'name',)
        widgets = {'recipe': forms.HiddenInput()}


IngredientFormset = inlineformset_factory(
    Recipe, Ingredient, form=IngredientForm, extra=4, can_delete=True)


class NewRecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = ('title',)

# class BaseRecipeFormSet(BaseInlineFormSet):
#     def add_fields(self, form, index):
#         super(BaseRecipeFormSet, self).add_fields(form, index)

#         form.nested = IngredientFormset(
#             instance=form.instance, data=form.data if form.is_bound else None, )


# RecipeFormSet = inlineformset_factory(
#     Recipe, Ingredient, extra=1)
