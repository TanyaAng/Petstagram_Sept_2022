from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views

from petstagram.accounts.forms import UserCreateForm, UserLoginForm, UserEditForm, UserDeleteForm

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


class UserDetailsView(views.DetailView):
    template_name = 'accounts/profile-details-page.html'
    model = UserModel
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['is_owner'] = self.request.user == self.object
        #Added .all() to make pets itterable
        pets = self.object.pet_set.all()
        context['pets'] = pets
        if pets:
            context['pets_count'] = pets.count()
        else:
            context['pets_count'] = 0

        # photos = self.object.photomodel_set.prefetch_related('like_set')
        photos = self.object.photomodel_set.all()
        context['photos'] = photos
        if photos:
            context['photos_count'] = photos.count()
            context['likes_count'] = sum([p.like_set.count() for p in photos])
        else:
            context['photos_count'] = 0
            context['likes_count'] = 0

        return context


class UserEditView(views.UpdateView):
    model = UserModel
    form_class = UserEditForm
    template_name = 'accounts/profile-edit-page.html'

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={'pk': self.request.user.pk})


class UserDeleteView(views.DeleteView):
    model = UserModel
    form_class = UserDeleteForm
    template_name = 'accounts/profile-delete-page.html'
    success_url = reverse_lazy('index')

    # def post(self, *args, pk):
    #     self.request.user.delete()
