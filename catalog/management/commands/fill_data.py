import json

from catalog.models import Category, Product
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def json_read_categories(self):
        with open('fixtures/categories.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data

    def json_read_products(self):
        with open('fixtures/products.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data

    def handle(self, *args, **options):
        # Delete all existing Products and Categories
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Load and create Category objects
        category_data = self.json_read_categories()
        category_for_create = []
        for data in category_data:
            category = Category(
                name=data['fields']['name'],
                description=data['fields']['description']
            )
            category_for_create.append(category)
        Category.objects.bulk_create(category_for_create)

        # Here I have to fetch categories again as they now have IDs assigned by the database !!!
        categories = {category.name: category for category in Category.objects.all()}

        # Load and create Product objects
        product_data = self.json_read_products()
        product_for_create = []

        for data in product_data:
            category_name = data['category_name']
            try:
                category = categories[category_name]
            except KeyError:
                self.stdout.write(self.style.ERROR(f"Category not found: {category_name}"))
                continue  # Skip this product if category not found
            product = Product(
                name=data.get('name', ''),
                description=data.get('description', ''),
                image=data.get('image', ''),
                price=data.get('price', ''),
                category=category
            )
            product_for_create.append(product)

        self.stdout.write(self.style.SUCCESS('Added categories and products to the database.'))
