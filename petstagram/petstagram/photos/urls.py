from django.urls import path, include

from petstagram.photos.views import photo_create, photo_details, photo_edit

urlpatterns = (
    path('add/', photo_create, name='photo create'),
    path('<int:pk>/',
         include(
             [
                 path('', photo_details, name='photo details'),
             path('edit/', photo_edit, name='photo edit'),
             # path('delete/', photo_delete, name='photo delete')
             ]
         ),
))

