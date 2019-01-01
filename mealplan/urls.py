from django.urls import path, include
from . import views

app_name = 'mealplan'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:user_id>/', views.profile, name='recipe_plan'),
    path('ingredients/', views.ingredient_page, name='ingredient_page'),
]