import csv

from django.core.management import BaseCommand
from recipes.models import Ingredient
class Command(BaseCommand):
    def handle(self, *args, **options):
        file = open('ingredients.csv', 'r')
        reader = csv.reader(file)
        bulk_list = []
        for row in reader:
            name, unit = [*row]
            bulk_list.append(Ingredient(name=name, unit=unit))
        Ingredient.objects.bulk_create(bulk_list)
        return (
            f'{Ingredient.objects.count()} - ингредиенты успешно созданы'
        )