from django.shortcuts import render


def pet_create(request):
    return render(request, 'pets/pet-add-page.html')


def pet_details(request, username='Gosho', pet_name='Pesho'):
    return render(request, 'pets/pet-details-page.html')


def pet_edit(request, username='Gosho', pet_name='Pesho'):
    return render(request, 'pets/pet-edit-page.html')


def pet_delete(request, username='Gosho', pet_name='Pesho'):
    return render(request, 'pets/pet-delete-page.html')
