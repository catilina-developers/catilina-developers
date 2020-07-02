from django.shortcuts import render
from django.http import HttpResponse
from .models import Customers

# Create your views here.

def home(request):
    return render(request, 'acc/index.html')


def about(request):
    return render(request, 'acc/about.html')


def blog(request):
    return render(request, 'acc/blog.html')


def contact(request):
    return render(request, 'acc/contact.html')


def portfolio(request):
    return render(request, 'acc/portfolio.html')


def prepros(request):
    return render(request, 'acc/prepros.html')


def services(request):
    return render(request, 'acc/services.html')


def showcase(request):
    return render(request, 'acc/showcase.html')


def form_submission(request):
    name = request.POST["cust_name"]
    email = request.POST["email"]
    message = request.POST["message"]
    subject = request.POST["subject"]
    customers = Customers(name=name, email=email, message=message, subject=subject)
    customers.save()
    return render(request, 'acc/contact.html')
