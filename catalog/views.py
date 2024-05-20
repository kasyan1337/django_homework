# Create your views here.
from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify
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
        obj = super().get_object(queryset=queryset)
        obj.view_count += 1
        if obj.view_count == 100:
            self.send_view_count_email(obj.title, obj.view_count)
        obj.save()
        return obj

    def send_view_count_email(self, blog_title, view_count):
        subject = f"Blog {blog_title} reached {view_count} views!"
        message = f"Congrats! Blog {blog_title} reached {view_count} views!"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [settings.EMAIL_HOST_USER]
        send_mail(subject, message, email_from, recipient_list, fail_silently=False)

class BlogCreateView(CreateView):
    model = Blog
    template_name = 'blog/blog_form.html'
    fields = ['title', 'content', 'preview', 'is_published']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.slug = slugify(self.object.title)
        self.object.save()
        return super().form_valid(form)

class BlogUpdateView(UpdateView):
    model = Blog
    template_name = 'blog/blog_form.html'
    fields = ['title', 'content', 'preview', 'is_published']

    def get_success_url(self):
        return reverse('catalog:blog_detail', kwargs={'slug': self.object.slug})

class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blog/blog_confirm_delete.html'
    success_url = reverse_lazy('catalog:blog_list')