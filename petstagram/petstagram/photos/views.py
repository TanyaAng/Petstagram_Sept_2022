from django.shortcuts import render


def photo_create(request):
    return render(request, 'photos/photo-add-page.html')


def photo_details(request, pk=1):
    return render(request, 'photos/photo-details-page.html')


def photo_edit(request, pk=1):
    return render(request, 'photos/photo-edit-page.html')
