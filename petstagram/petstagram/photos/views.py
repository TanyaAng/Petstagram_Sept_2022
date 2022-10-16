from django.shortcuts import render

from petstagram.photos.models import PhotoModel


def photo_create(request):
    return render(request, 'photos/photo-add-page.html')


def photo_details(request, pk):
    photo = PhotoModel.objects.get(pk=pk)
    likes = photo.like_set.all()
    comments = photo.comment_set.all()
    context = {
        'photo': photo,
        'likes': likes,
        'comments': comments,
        'show_comments': True,
    }
    return render(request, 'photos/photo-details-page.html', context)


def photo_edit(request, pk):
    return render(request, 'photos/photo-edit-page.html')
