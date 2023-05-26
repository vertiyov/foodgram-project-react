import csv

from django.core.management.base import BaseCommand, CommandError

from recipes.models import Ingredient


class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            with open('ingredients.csv', 'r') as file:
                reader = csv.reader(file)
                bulk_list = []
                for row in reader:
                    name, unit = [*row]
                    bulk_list.append(Ingredient(name=name, unit=unit))
                Ingredient.objects.bulk_create(bulk_list)
                return (
                    f'{Ingredient.objects.count()} - ингредиенты созданы'
                )
        except FileNotFoundError:
            raise CommandError('Файл не найден')
