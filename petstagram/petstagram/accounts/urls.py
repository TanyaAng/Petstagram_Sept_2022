from django.urls import path, include

from petstagram.accounts.views import profile_details, profile_edit, profile_delete, \
    SignUpView, SingInView, SingOutView



urlpatterns = (
    path('register/', SignUpView.as_view(), name='register'),
    path('login/', SingInView.as_view(), name='login'),
    path('logout/', SingOutView.as_view(), name='logout'),

    path('profile/<int:pk>/',
         include([
             path('', profile_details, name='profile details'),
             path('edit/', profile_edit, name='profile edit'),
             path('delete/', profile_delete, name='profile delete'),
         ])),
)
