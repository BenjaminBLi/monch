from django.db import models
from django.utils.timezone import now as current_date

"""
quick note: I don't know how many to many fields work so if this breaks I'm sorry xd
"""


class Ingredient(models.Model):
    quantity = models.IntegerField()
    ingredient_name = models.CharField(max_length=30)
    expiry_date = models.DateField(default=current_date)

    def __str__(self):
        return self.ingredient_name


class Fridge(models.Model):
    contents = models.ManyToManyField(Ingredient, verbose_name="contents of fridge")

    def __str(self):
        return self.contents


class Recipe(models.Model):
    ingredients = models.ManyToManyField(Ingredient, verbose_name="list of ingredients")
    recipe_name = models.CharField(max_length=30)
    meal = models.IntegerField()
    eat_date = models.DateField(default=current_date)

    def __str__(self):
        return self.recipe_name


class User(models.Model):
    recipes = models.ManyToManyField(Recipe, verbose_name="list of recipes")
    username = models.CharField(max_length=30)
    user_fridge = models.ForeignKey(Fridge, on_delete=models.CASCADE)

    def __str__(self):
        return self.username
