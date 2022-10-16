from django.shortcuts import render

from petstagram.pets.models import Pet


def pet_create(request):
    return render(request, 'pets/pet-add-page.html')


def pet_details(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    all_pet_photos = pet.photomodel_set.all()
    context = {
        'pet': pet,
        'pet_photos': all_pet_photos,
    }
    return render(request, 'pets/pet-details-page.html', context)


def pet_edit(request, username, pet_slug):
    return render(request, 'pets/pet-edit-page.html')


def pet_delete(request, username, pet_slug):
    return render(request, 'pets/pet-delete-page.html')
