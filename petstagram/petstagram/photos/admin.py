from django.contrib import admin

from petstagram.photos.models import PhotoModel


@admin.register(PhotoModel)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_of_publication', 'description', 'get_tagged_pets')

    @staticmethod
    def get_tagged_pets(obj):
        return ', '.join([str(pet) for pet in obj.tagged_pets.all()])
