from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Pet
from .forms import PetForm


@login_required
def my_pets_view(request):
    """List all pets belonging to the logged-in user."""
    pets = Pet.objects.filter(owner=request.user)
    return render(request, 'patients/my_pets.html', {'pets': pets})


@login_required
def add_pet_view(request):
    """Add a new pet for the logged-in user."""
    if request.method == 'POST':
        form = PetForm(request.POST)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.owner = request.user
            pet.save()
            messages.success(request, f'{pet.name} has been registered!')
            return redirect('patients:my_pets')
    else:
        form = PetForm()
    return render(request, 'patients/pet_form.html', {'form': form, 'action': 'Register'})


@login_required
def edit_pet_view(request, pk):
    """Edit an existing pet."""
    pet = get_object_or_404(Pet, pk=pk, owner=request.user)
    if request.method == 'POST':
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            messages.success(request, f'{pet.name} has been updated!')
            return redirect('patients:my_pets')
    else:
        form = PetForm(instance=pet)
    return render(request, 'patients/pet_form.html', {'form': form, 'action': 'Update', 'pet': pet})


@login_required
def delete_pet_view(request, pk):
    """Delete a pet."""
    pet = get_object_or_404(Pet, pk=pk, owner=request.user)
    if request.method == 'POST':
        name = pet.name
        pet.delete()
        messages.success(request, f'{name} has been removed.')
        return redirect('patients:my_pets')
    return render(request, 'patients/pet_confirm_delete.html', {'pet': pet})
