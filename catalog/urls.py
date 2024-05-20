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

# CBV
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('contacts/', views.ContactView.as_view(), name='contacts'),
    path('product_page_details/<int:pk>/', views.ProcuctDetailView.as_view(), name='product_page_details'),
]

# FBV
# urlpatterns = [
#     path('', views.home, name='home'),
#     path('contacts/', views.contact, name='contacts'),
#     path('product_page_details/<int:pk>/', views.product_detail, name='product_page_details'),
# ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
