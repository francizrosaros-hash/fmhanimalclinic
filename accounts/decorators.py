from functools import wraps

from django.shortcuts import redirect
from django.http import HttpResponseForbidden


def role_required(*roles):
    """
    Decorator that restricts a view to users whose role is in the given list.

    Usage:
        @login_required
        @role_required(User.Role.ADMIN, User.Role.BRANCH_ADMIN)
        def admin_only_view(request):
            ...
    """
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if request.user.is_authenticated and request.user.role in roles:
                return view_func(request, *args, **kwargs)
            return HttpResponseForbidden('You do not have permission to access this page.')
        return wrapper
    return decorator
