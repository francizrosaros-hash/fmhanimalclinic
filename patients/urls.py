from django.urls import path
from . import views

app_name = 'patients'

urlpatterns = [
    path('my-pets/', views.my_pets_view, name='my_pets'),
    path('add/', views.add_pet_view, name='add_pet'),
    path('<int:pk>/edit/', views.edit_pet_view, name='edit_pet'),
    path('<int:pk>/delete/', views.delete_pet_view, name='delete_pet'),
]
