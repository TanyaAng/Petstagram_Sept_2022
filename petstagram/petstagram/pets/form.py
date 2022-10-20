from django import forms

from petstagram.core.form_mixins import DisableFormMixin
from petstagram.pets.models import Pet


class BasePetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ('name', 'date_of_birth', 'personal_photo')

        labels = {
            'name': 'Pet name',
            'date_of_birth': 'Date of birth',
            'personal_photo': 'Link to image',
        }

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Pet name'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'personal_photo': forms.TextInput(attrs={'placeholder': 'Link to image'}),
        }


class CreatePetForm(BasePetForm):
    pass


class EditPetForm(BasePetForm):
    pass


class DeletePetForm(DisableFormMixin, BasePetForm):
    disable_fields = ('name', 'date_of_birth', 'personal_photo')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        else:
            pass
        return self.instance
