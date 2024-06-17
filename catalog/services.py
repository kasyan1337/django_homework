from django.core.cache import cache

from catalog.models import Product
from django_homework.settings import CACHE_ENABLED


def get_product_list_from_cache():
    """
    Get product list from cache
    """
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = 'product_list'
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set("product_list", products)
    return products
