from django import forms
from .models import Pet


class PetForm(forms.ModelForm):
    """Form for creating and editing a pet."""

    class Meta:
        model = Pet
        fields = ['name', 'species', 'breed', 'age', 'sex', 'color']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'e.g. Buddy'}),
            'species': forms.TextInput(attrs={'placeholder': 'e.g. Dog, Cat, Bird'}),
            'breed': forms.TextInput(attrs={'placeholder': 'e.g. Golden Retriever'}),
            'age': forms.NumberInput(attrs={'placeholder': 'Age in years', 'min': 0}),
            'color': forms.TextInput(attrs={'placeholder': 'e.g. Brown & White'}),
        }
