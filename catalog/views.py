# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView

from .models import Product, Blog


# CBV
class HomeView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'


class ContactView(TemplateView):
    template_name = 'catalog/contact.html'

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Do something with the data
        print(f"Received contact info - Name: {name}, Phone: {phone}, Message: {message}")

        return self.render_to_response({self.get_context_data()})


class ProcuctDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


# FBV
# def home(request):
#     products = Product.objects.all()  # Fetch all products, otherwise it will be empty
#     return render(request, 'catalog/home.html', {'products': products})

# def contact(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#
#         # Do something with the data
#         print(f"Received contact info - Name: {name}, Phone: {phone}, Message: {message}")
#
#     return render(request, 'catalog/contact.html')


# from django.shortcuts import render, get_object_or_404
# def product_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {
#         'product': product
#     }
#     return render(request, 'catalog/product_detail.html', context)

class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blog_list.html'
    queryset = Blog.objects.filter(is_published=True)

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'

    def get_object(self, queryset=None):
        obj = super().get_object()
        obj.view_count += 1
        obj.save()
        return obj


class BlogCreateView(CreateView):
    model = Blog
    template_name = 'blog/blog_form.html'
    fields = ['title', 'content', 'preview', 'is_published']
    success_url = reverse_lazy('catalog:blog_list')

class BlogUpdateView(UpdateView):
    model = Blog
    template_name = 'blog/blog_form.html'
    fields = ['title', 'content', 'preview', 'is_published']
    success_url = reverse_lazy('catalog:blog_list')

class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blog/blog_confirm_delete.html'
    success_url = reverse_lazy('catalog:blog_list')