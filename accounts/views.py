from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def login_view(request):
    """Login page view"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully logged in!')
            return redirect('landing_page')
        else:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'accounts/login.html')

def register_view(request):
    """Register page view"""
    if request.method == 'POST':
        # Registration logic will be implemented later with forms
        pass
    
    return render(request, 'accounts/register.html')

def logout_view(request):
    """Logout view"""
    logout(request)
    messages.success(request, 'Successfully logged out!')
    return redirect('landing_page')
