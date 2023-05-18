import csv

from django.core.management import BaseCommand
from recipes.models import Ingredient

class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('ingredients.csv', 'r') as file:
            reader = csv.reader(file)

            for row in reader:
                ingredient, created = Ingredient.objects.get_or_create(
                    name = row[0],
                    unit = row[1],
                )
                if created:
                    print(f'{ingredient.id} создан')
                else:
                    print('Error')