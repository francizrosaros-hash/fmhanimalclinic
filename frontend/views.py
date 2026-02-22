from django.shortcuts import render

# Create your views here.

def home_view(request):
    """Home page view"""
    return render(request, 'frontend/home.html')

def about_view(request):
    """About page view"""
    return render(request, 'frontend/about.html')

def services_view(request):
    """Services page view"""
    return render(request, 'frontend/services.html')

def contact_view(request):
    """Contact page view"""
    return render(request, 'frontend/contact.html')
