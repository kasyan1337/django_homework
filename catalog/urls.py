"""
Added manually
Here is a copypaste from the urls.py file from the other directory:
Admin doesn't have to be here.
"""
# from django.contrib import admin
from django.urls import path, include
from .apps import CatalogConfig
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = CatalogConfig.name

urlpatterns = [
    path('', views.home, name='home'),
    path('contacts/', views.contact, name='contacts'), # Changed to 'contacts/' because in the contact.html file
    # the form action is set to 'contacts/'
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

