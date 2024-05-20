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
    path('blog/', views.BlogListView.as_view(), name='blog_list'),
    path('blog/add/', views.BlogCreateView.as_view(), name='blog_add'),
    path('blog/<slug:slug>/', views.BlogDetailView.as_view(), name='blog_detail'),
    path('blog/edit/<slug:slug>/', views.BlogUpdateView.as_view(), name='blog_edit'),
    path('blog/delete/<slug:slug>/', views.BlogDeleteView.as_view(), name='blog_delete'),
]

# FBV
# urlpatterns = [
#     path('', views.home, name='home'),
#     path('contacts/', views.contact, name='contacts'),
#     path('product_page_details/<int:pk>/', views.product_detail, name='product_page_details'),
# ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
