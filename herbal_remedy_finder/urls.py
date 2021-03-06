from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('all/', views.recipe_list, name='recipe_list'),
    path('detail/<int:pk>', views.recipe_detail, name='recipe_detail'),
    path('search', views.search_results, name='search_results'),
    path('ingredient_search', views.search_results_i, name='search_results_i'),
    path('info/<int:pk>', views.additional_info, name='additional_info'),
    path('resources/', views.resources, name='resources'),
    path('instructional/<int:pk>', views.instructional_detail,
         name='instructional_detail')
]
