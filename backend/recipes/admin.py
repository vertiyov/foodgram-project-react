from django.contrib import admin

from .models import Ingredient, Tag, Recipe, RecipeIngredient

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'unit')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'color')

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('author', 'name', 'description')

@admin.register(RecipeIngredient)
class RecipeIngredient(admin.ModelAdmin):
    list_display = ('recipe', 'ingredient', 'amount')