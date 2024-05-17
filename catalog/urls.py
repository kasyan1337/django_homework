"""
Added manually
Here is a copypaste from the urls.py file from the other directory:
Admin doesn't have to be here.
"""
from django.conf import settings
from django.conf.urls.static import static
# from django.contrib import admin
from django.urls import path

from . import views
from .apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', views.home, name='home'),
    path('contacts/', views.contact, name='contacts'),
    # Not needed anymore because I added the product_list to the home page
    # path('product_list/', views.product_list, name='product_list'),
    path('product_page_details/<int:pk>/', views.product_detail, name='product_page_details'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
