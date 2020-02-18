from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.recipe_list, name='recipe_list'),
    # url view name for redirects
    path('detail/<int:pk>', views.recipe_detail, name='recipe_detail'),
    path('new', views.recipe_new, name='recipe_new')
    # path('new/recipe', views.recipe_create, name='recipe_create')
]
