"""
Added manually
Here is a copypaste from the urls.py file from the other directory:
Admin doesn't have to be here.
"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.decorators.cache import cache_page

from . import views
from .apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('contacts/', views.ContactView.as_view(), name='contacts'),
    path('product_page_details/<int:pk>/', views.ProductDetailView.as_view(), name='product_page_details'),
    path('blog/', views.BlogListView.as_view(), name='blog_list'),
    path('blog/add/', views.BlogCreateView.as_view(), name='blog_add'),
    path('blog/<slug:slug>/', views.BlogDetailView.as_view(), name='blog_detail'),
    path('blog/edit/<slug:slug>/', views.BlogUpdateView.as_view(), name='blog_edit'),
    path('blog/delete/<slug:slug>/', views.BlogDeleteView.as_view(), name='blog_delete'),
    path('product/<int:pk>/', cache_page(60)(views.ProductDetailView.as_view()), name='product-detail'),
    path('product/new/', views.ProductCreateView.as_view(), name='product-create'),
    path('product/<int:pk>/edit/', cache_page(60)(views.ProductUpdateView.as_view()), name='product-update'),
    path('product/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product-delete'),
    path('version/new/', views.VersionCreateView.as_view(), name='version-create'),
    path('version/<int:pk>/edit/', views.VersionUpdateView.as_view(), name='version-update'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
