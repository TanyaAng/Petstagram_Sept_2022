from django.shortcuts import render, redirect

from petstagram.photos.form import CreatePhotoForm, EditPhotoForm
from petstagram.photos.models import PhotoModel


def photo_details(request, pk):
    photo = PhotoModel.objects.filter(pk=pk).get()
    likes = photo.like_set.all()
    comments = photo.comment_set.all()
    context = {
        'photo': photo,
        'likes': likes,
        'username': 'Tanya',
        'comments': comments,
        'show_comments': True,
    }
    return render(request, 'photos/photo-details-page.html', context)


def photo_create(request):
    if request.method == 'GET':
        form = CreatePhotoForm()
    else:
        form = CreatePhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form,
    }
    return render(request, 'photos/photo-add-page.html', context)


def photo_edit(request, pk):
    photo = PhotoModel.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = EditPhotoForm(instance=photo)
    else:
        form = EditPhotoForm(request.POST, instance=photo)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form,
        'photo_pk': pk,
    }
    return render(request, 'photos/photo-edit-page.html', context)


def photo_delete(request, pk):
    photo = PhotoModel.objects.filter(pk=pk).get()
    photo.delete()
    return redirect('index')
