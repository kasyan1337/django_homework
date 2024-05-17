# Create your views here.
from .models import Product


def home(request):
    products = Product.objects.all()  # Fetch all products, otherwise it will be empty
    return render(request, 'catalog/home.html', {'products': products})


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Do something with the data
        print(f"Received contact info - Name: {name}, Phone: {phone}, Message: {message}")

    return render(request, 'catalog/contact.html')


# Not needed anymore because I added the product_list to the home page
# def product_list(request, pk=1):
#     products = Product.objects.all()
#     context = {
#         'products': products
#     }
#     return render(request, 'catalog/product_list.html', context)


from django.shortcuts import render, get_object_or_404


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product
    }
    return render(request, 'catalog/product_detail.html', context)
