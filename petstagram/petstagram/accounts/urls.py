from django.urls import path, include

from petstagram.accounts.views import register_user, login_user, profile_details, profile_edit, profile_delete

urlpatterns = (
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('profile/<int:pk>/',
         include([
             path('', profile_details, name='profile details'),
             path('edit/', profile_edit, name='profile edit'),
             path('delete/', profile_delete, name='profile delete'),
         ])),
)
