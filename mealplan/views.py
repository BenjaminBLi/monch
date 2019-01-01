from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

"""
what each view is for/how it links to each other

index: default landing page
contains:
    if the user is not logged in:
        user registration page
    else:
        links to go to views for:
            current recipe plan
            ingredient entering


"""


def index(request):
    return HttpResponse("woah you're at our index page")


def profile(request, profile_id):
    return HttpResponse("let's take a look at ur schedule")


def ingredient_page(request):
    return HttpResponse("ingredients page")
