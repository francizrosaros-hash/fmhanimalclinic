from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import User
from .decorators import role_required


def login_view(request):
    """Login page — redirects to correct portal after login."""
    if request.user.is_authenticated:
        if request.user.is_clinic_staff():
            return redirect('admin_dashboard')
        return redirect('user_dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully logged in!')

            if user.is_clinic_staff():
                return redirect('admin_dashboard')
            return redirect('user_dashboard')
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


@login_required
def user_dashboard_view(request):
    """User portal dashboard."""
    return render(request, 'accounts/user_dashboard.html')


@login_required
@role_required(User.Role.STAFF, User.Role.VETERINARIAN, User.Role.BRANCH_ADMIN, User.Role.ADMIN)
def admin_dashboard_view(request):
    """Admin portal dashboard — restricted to clinic staff roles."""
    return render(request, 'accounts/admin_dashboard.html')
