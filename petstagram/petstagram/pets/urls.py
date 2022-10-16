from django.urls import path, include

from petstagram.pets.views import pet_create, pet_details, pet_edit, pet_delete

urlpatterns = (
    path('add/', pet_create, name = 'pet create'),
    path('<str:username>/pet/<slug:pet_slug>/',
         include([
             path('', pet_details, name='pet details'),
             path('edit/', pet_edit, name='pet edit'),
             path('delete/', pet_delete, name='pet delete'),
         ]))
)