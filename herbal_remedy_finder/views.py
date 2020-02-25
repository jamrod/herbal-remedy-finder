from django.shortcuts import render, redirect
from django.db.models import Q

from .models import Recipe, Ingredient, Info, Instructional


def home(request):
    return render(request, 'finder/home.html')


def search_results(request):
    query = request.GET.get('q')
    recipe = Recipe.objects.filter(
        Q(title__icontains=query) | Q(tags__icontains=query)
    ).order_by('title')
    if len(recipe) == 0:
        return render(request, 'finder/home.html', {'message': 'fail'})
    return render(request, 'finder/recipe_list.html', {'recipes': recipe})


def search_results_i(request):
    query = request.GET.get('q')
    ingredients = Ingredient.objects.filter(
        Q(name__icontains=query)
    ).order_by('recipe')
    list = []
    for i in ingredients:
        list.append(i.recipe)
    # recipes = list.sort(key=lambda x: x.title)
    if len(list) == 0:
        return render(request, 'finder/home.html', {'message': 'fail'})
    return render(request, 'finder/recipe_list.html', {'recipes': list})


def recipe_list(request):
    recipe = Recipe.objects.all().order_by('title')
    return render(request, 'finder/recipe_list.html', {'recipes': recipe})


def recipe_detail(request, pk):
    recipe = Recipe.objects.get(id=pk)
    return render(request, 'finder/recipe_detail.html', {'recipe': recipe})


def additional_info(request, pk):
    info = Info.objects.get(id=pk)
    return render(request, 'finder/additional_info.html', {'info': info})


def resources(request):
    items = Info.objects.all()
    instructions = Instructional.objects.all()
    return render(request, 'finder/resources.html', {'items': items, 'instructions': instructions})


def instructional_detail(request, pk):
    instructions = Instructional.objects.get(id=pk)
    return render(request, 'finder/instructional_detail.html', {'instructions': instructions})
