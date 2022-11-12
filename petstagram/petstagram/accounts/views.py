from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views

from petstagram.accounts.forms import UserCreateForm, UserLoginForm

UserModel = get_user_model()


class SignUpView(views.CreateView):
    model = UserModel
    form_class = UserCreateForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('login')


class SingInView(auth_views.LoginView):
    form_class = UserLoginForm
    template_name = 'accounts/login-page.html'
    success_url = reverse_lazy('index')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class SingOutView(auth_views.LogoutView):
    next_page = reverse_lazy('login')


def profile_details(request, pk):
    context = {
        'pk': pk,
    }
    return render(request, 'accounts/profile-details-page.html', context)


def profile_edit(request, pk):
    return render(request, 'accounts/profile-edit-page.html')


def profile_delete(request, pk):
    return render(request, 'accounts/profile-delete-page.html')
