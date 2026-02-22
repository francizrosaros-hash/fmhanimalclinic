from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login_page'),
    path('register/', views.register_view, name='register_page'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.user_dashboard_view, name='user_dashboard'),
    path('admin-dashboard/', views.admin_dashboard_view, name='admin_dashboard'),
]
