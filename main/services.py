# main/services.py
from django.core.cache import cache
from .models import Category


def get_cached_categories():
    cached_categories = cache.get('categories')
    if not cached_categories:
        categories = Category.objects.all()
        cache.set('categories', categories, timeout=3600)  # Кеширование на 1 час
        return categories
    return cached_categories
