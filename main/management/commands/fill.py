from django.core.management import BaseCommand

from main.models import Category
from main.models import Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        category_list = [
            {'name': 'Овощи', 'description': 'Морковь, картофель, капуста и др.'},
            {'name': 'Мясо', 'description': 'Говядина, свинина и др.'},
            {'name': 'Молочные', 'description': 'Молоко, кефир, сыр и др.'},
        ]

        category_for_create = []

        for category_item in category_list:
            category_for_create.append(
                Category(**category_item)
            )

        Category.objects.all().delete()
        Category.objects.bulk_create(category_for_create)

        product_list = [
            {'name': 'сметана', 'description': 'Лучшая сметана', 'price': 150.00, 'category': Category.objects.get(name='Молочные')},
            {'name': 'кефир', 'description': 'Лучший кефир', 'price': 75.40, 'category': Category.objects.get(name='Молочные')},
            {'name': 'свёкла', 'description': 'Лучшая свёкла', 'price': 50.00, 'category': Category.objects.get(name='Овощи')},
            {'name': 'говядина', 'description': 'Лучшая говядина', 'price': 550.55, 'category': Category.objects.get(name='Мясо')},
        ]

        product_for_create = []

        for product_item in product_list:
            product_for_create.append(
                Product(**product_item)
            )

        Product.objects.all().delete()
        Product.objects.bulk_create(product_for_create)