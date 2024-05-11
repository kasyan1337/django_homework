"""
Added manually
Here is a copypaste from the urls.py file from the other directory:
Admin doesn't have to be here.
"""
# from django.contrib import admin
from django.urls import path, include
from .apps import CatalogConfig
from . import views

app_name = CatalogConfig.name

urlpatterns = [
    path('', views.home, name='home'),
    path('contacts/', views.contact, name='contacts'), # Changed to 'contacts/' because in the contact.html file
    # the form action is set to 'contacts/'
]
