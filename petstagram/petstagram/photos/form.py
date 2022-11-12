from django import forms

from petstagram.photos.models import PhotoModel


class CreatePhotoForm(forms.ModelForm):
    class Meta:
        model = PhotoModel
        fields = '__all__'
        exclude = ('user',)
        labels = {
            'photo': 'Photo file',
            'tagged_pets': 'Tag pets',
        }


class EditPhotoForm(forms.ModelForm):
    class Meta:
        model = PhotoModel
        exclude = ('photo', 'user',)
