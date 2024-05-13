# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages


def home(request):
    return render(request, 'catalog/home.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Do something with the data
        print(f"Received contact info - Name: {name}, Phone: {phone}, Message: {message}")
        # messages.success(request, 'Thank you for your message!') # Added a success message for the user
        # commented, would have to edit the html to make it work

        # return redirect('contact')  # Redirect to the same page or to a success page

    return render(request, 'catalog/contact.html')
