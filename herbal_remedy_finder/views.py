from django.shortcuts import render, redirect
from django.forms.formsets import formset_factory

from .models import Recipe
from .forms import RecipeForm, IngredientForm, IngredientFormset, NewRecipeForm


def recipe_list(request):
    recipe = Recipe.objects.all()
    return render(request, 'finder/recipe_list.html', {'recipes': recipe})


def recipe_detail(request, pk):
    recipe = Recipe.objects.get(id=pk)
    return render(request, 'finder/recipe_detail.html', {'recipe': recipe})


def recipe_new(request):
    if request.method == 'POST':
        form = NewRecipeForm(request.POST)
        if form.isValid():
            recipe = form.save()
            return redirect('recipe_create', pk=recipe.id)
    else:
        form = NewRecipeForm()
    return render(request, 'finder/new_recipe_form.html', {'form': form})


def recipe_create(request, pk):
    recipe = Recipe.objects.get(id=pk)
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        formset = IngredientFormset(request.POST)
        if form.is_valid():
            recipe = form.save()
            if formset.is_valid():
                for item in formset:
                    item = form.save()
                return redirect('recipe_detail', pk=recipe.id)
    else:
        form = RecipeForm(initial={'title': recipe.title})
        formset = IngredientFormset(initial={'recipe': recipe.id})
    return render(request, 'finder/recipe_form.html', {'form': form, 'formset': formset})


# def recipe_new(request):
#     if request.method == 'POST':
#         form = RecipeForm(request.POST)
#         formset = IngredientFormset(request.POST)
#         if form.is_valid():
#             recipe = form.save()
#             if formset.is_valid():
#                 ingredients = []
#                 for i in formset:


#             return redirect('recipe_detail', pk=recipe.id)
#     else:
#         form = RecipeForm()
#         formset = IngredientFormset

#     return render(request, 'finder/recipe_form.html', {'form': form})


def recipe_edit(request, pk):
    recipe = Recipe.objects.get(id=pk)
    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            timeline = form.save()
            return redirect('recipe_detail', pk=recipe.id)
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'finder/recipe_form.html', {'form': form})
