from django.shortcuts import render, redirect

from petstagram.pets.form import CreatePetForm, EditPetForm, DeletePetForm
from petstagram.pets.models import Pet


def pet_details(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    all_pet_photos = pet.photomodel_set.all()
    context = {
        'pet': pet,
        'pet_photos': all_pet_photos,
        'username': username,
        'hide_comment_form': True,

    }
    return render(request, 'pets/pet-details-page.html', context)


def pet_create(request):
    if request.method == 'GET':
        form = CreatePetForm()
    else:
        form = CreatePetForm(request.POST)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.user = request.user
            pet.save()
            return redirect('profile details', pk=request.user.pk)

    context = {
        'form': form,
    }
    return render(request, 'pets/pet-add-page.html', context)


def pet_edit(request, username, pet_slug):
    pet = Pet.objects.filter(slug=pet_slug, user__username=username).get()
    if request.method == 'GET':
        form = EditPetForm(instance=pet)
    else:
        form = EditPetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pet details', username=username, pet_slug=pet_slug)

    context = {
        'form': form,
        'username': username,
        'pet': pet,
    }
    return render(request, 'pets/pet-edit-page.html', context)


def pet_delete(request, username, pet_slug):
    pet = Pet.objects.filter(slug=pet_slug, user__username=username).get()
    if request.method == 'GET':
        form = DeletePetForm(instance=pet)
    else:
        form = DeletePetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('profile details', pk=request.user.pk)

    context = {
        'form': form,
        'username': username,
        'pet': pet,
    }
    return render(request, 'pets/pet-delete-page.html', context)
