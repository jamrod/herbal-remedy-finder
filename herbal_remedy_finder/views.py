from django.shortcuts import render, redirect
from .models import Recipe
from .forms import RecipeForm


def recipe_list(request):
    recipe = Recipe.objects.all()
    return render(request, 'finder/recipe_list.html', {'recipes': recipe})


def recipe_detail(request, pk):
    recipe = Recipe.objects.get(id=pk)
    return render(request, 'finder/recipe_detail.html', {'recipe': recipe})


def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            timeline = form.save()
            return redirect('recipe_detail', pk=recipe.id)
    else:
        form = RecipeForm()
    return render(request, 'finder/recipe_form.html', {'form': form})


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
