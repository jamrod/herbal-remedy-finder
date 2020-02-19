from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.recipe_list, name='recipe_list'),
    path('detail/<int:pk>', views.recipe_detail, name='recipe_detail'),
    path('new', views.Recipe_Create.as_view(), name='recipe_create'),
    path('edit/<int:pk>', views.Recipe_Edit.as_view(), name='recipe_edit')
]
