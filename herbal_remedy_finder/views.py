from django.shortcuts import render, redirect
from django.urls import reverse
from django.forms.models import inlineformset_factory
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
import random
from django.db.models import Q

from .models import Recipe, Ingredient
from .forms import RecipeForm, IngredientForm, IngredientFormset, NewRecipeForm


def home(request):
    return render(request, 'finder/home.html')


def search_results(request):
    query = request.GET.get('q')
    recipe = Recipe.objects.filter(
        Q(title__icontains=query) | Q(tags__icontains=query)
    )
    return render(request, 'finder/recipe_list.html', {'recipes': recipe})


def search_results_i(request):
    query = request.GET.get('q')
    ingredients = Ingredient.objects.filter(
        Q(name__icontains=query)
    )
    recipes = []
    for i in ingredients:
        recipes.append(i.recipe)
    return render(request, 'finder/recipe_list.html', {'recipes': recipes})


def recipe_list(request):
    recipe = Recipe.objects.all()
    return render(request, 'finder/recipe_list.html', {'recipes': recipe})


def recipe_detail(request, pk):
    recipe = Recipe.objects.get(id=pk)
    return render(request, 'finder/recipe_detail.html', {'recipe': recipe})


class Recipe_Create(CreateView):
    model = Recipe
    template_name = 'finder/recipe_form.html'
    fields = ['title', 'description', 'instructions', 'pic', 'tags']

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data["ingredients"] = IngredientFormset(self.request.POST)
        else:
            data["ingredients"] = IngredientFormset()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        ingredients = context["ingredients"]
        self.object = form.save()
        if ingredients.is_valid():
            ingredients.instance = self.object
            ingredients.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('recipe_list')


class Recipe_Edit(UpdateView):
    model = Recipe
    template_name = 'finder/recipe_form.html'
    fields = ['title', 'description', 'instructions', 'pic', 'tags']

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data["ingredients"] = IngredientFormset(
                self.request.POST, instance=self.object)
        else:
            data["ingredients"] = IngredientFormset(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        ingredients = context["ingredients"]
        self.object = form.save()
        if ingredients.is_valid():
            ingredients.instance = self.object
            ingredients.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('recipe_detail', kwargs={'pk': self.object.id})


def recipe_edit(request, pk):
    recipe = Recipe.objects.get(id=pk)
    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            recipe = form.save()
            return redirect('recipe_detail', pk=recipe.id)
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'finder/recipe_form.html', {'form': form})
