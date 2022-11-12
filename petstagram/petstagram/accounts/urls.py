from django.urls import path, include

from petstagram.accounts.views import SignUpView, SingInView, SingOutView, UserEditView, \
    UserDeleteView, UserDetailsView

urlpatterns = (
    path('register/', SignUpView.as_view(), name='register'),
    path('login/', SingInView.as_view(), name='login'),
    path('logout/', SingOutView.as_view(), name='logout'),

    path('profile/<int:pk>/',
         include([
             path('', UserDetailsView.as_view(), name='profile details'),
             path('edit/', UserEditView.as_view(), name='profile edit'),
             path('delete/', UserDeleteView.as_view(), name='profile delete'),
         ])),
)
