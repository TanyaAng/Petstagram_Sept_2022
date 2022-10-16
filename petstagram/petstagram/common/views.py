from django.shortcuts import render, redirect, resolve_url
from pyperclip import copy

from petstagram.common.models import Like
from petstagram.photos.models import PhotoModel


def index(request):
    photos = PhotoModel.objects.all()
    context = {
        'photos': photos,
        'show_comments':False,
    }
    return render(request, 'common/home-page.html', context)


def like_functionality(request, photo_id):
    photo = PhotoModel.objects.get(id=photo_id)
    photo_likes = Like.objects.filter(to_photo_id=photo_id).first()
    if photo_likes:
        photo_likes.delete()
    else:
        like=Like(to_photo=photo)
        like.save()
    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')

def copy_to_clipboard(request, photo_id):
    copy(request.META['HTTP_HOST']+resolve_url('photo details', photo_id))
    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')

