from django.shortcuts import render, redirect, resolve_url
from pyperclip import copy

from petstagram.common.forms import CreateCommentForm, SearchForm
from petstagram.common.models import Like
from petstagram.photos.models import PhotoModel


def index(request):
    photos = PhotoModel.objects.all()
    comment_form = CreateCommentForm()
    search_form = SearchForm()
    user = request.user
    all_liked_photos_of_user = [like.to_photo_id for like in user.like_set.all()]
    if request.method == 'POST':
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            photos = photos.filter(tagged_pets__name__icontains=search_form.cleaned_data['pet_name'])
    context = {
        'photos': photos,
        'liked_photos': all_liked_photos_of_user,

        'comment_form': comment_form,
        'search_form': search_form,

        'show_comments': False,
    }
    return render(request, 'common/home-page.html', context)


def like_functionality(request, photo_id):
    photo = PhotoModel.objects.get(id=photo_id)
    photo_likes = Like.objects.filter(to_photo_id=photo_id, user=request.user).first()
    if photo_likes:
        photo_likes.delete()
    else:
        like = Like(to_photo=photo, user=request.user)
        like.save()
    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')


def copy_to_clipboard(request, photo_id):
    copy(request.META['HTTP_HOST'] + resolve_url('photo details', photo_id))
    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')


def comment_photo(request, photo_id):
    photo = PhotoModel.objects.filter(pk=photo_id).get()
    form = CreateCommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.to_photo = photo
        comment.user = request.user
        comment.save()
        return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')
