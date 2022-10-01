from django.shortcuts import render


def register(request):
    return render(request, 'accounts/register-page.html')

def login (request):
    return render (request, 'accounts/login-page.html')

def profile_details(request, pk=1):
    return render (request, 'accounts/profile-details-page.html')

def profile_edit(request, pk=1):
    return render (request, 'accounts/profile-edit-page.html')

def profile_delete(request, pk=1):
    return render (request, 'accounts/profile-delete-page.html')
