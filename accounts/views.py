from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import User
from .decorators import role_required
from .forms import PetOwnerRegistrationForm
from branches.models import Branch


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
            messages.success(request, 'Successfully logged in.')

            if user.is_clinic_staff():
                return redirect('admin_dashboard')
            return redirect('user_dashboard')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'accounts/login.html')


def register_view(request):
    """Register page view for Pet Owner registration"""
    if request.method == 'POST':
        form = PetOwnerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Auto-login after registration
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('select_branch')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = PetOwnerRegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})


@login_required
def select_branch_view(request):
    """Branch selection page — shown after pet owner registration."""
    branches = Branch.objects.filter(is_active=True)

    if request.method == 'POST':
        branch_id = request.POST.get('branch_id')
        if branch_id:
            branch = get_object_or_404(Branch, id=branch_id, is_active=True)
            request.user.branch = branch
            request.user.save(update_fields=['branch'])
            messages.success(request, f'Welcome! You are now registered at {branch.name}.')
        return redirect('user_dashboard')

    return render(request, 'accounts/select_branch.html', {'branches': branches})


def logout_view(request):
    """Logout view"""
    logout(request)
    messages.success(request, 'You have been successfully logged out.')
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
