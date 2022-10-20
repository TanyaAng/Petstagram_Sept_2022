from django.urls import path

from petstagram.common.views import index, like_functionality, copy_to_clipboard, comment_photo

urlpatterns = (
    path('', index, name='index'),
    path('like/<int:photo_id>/', like_functionality, name='like'),
    path('share/<int:photo_id>/', copy_to_clipboard, name='share'),
    path('comment/<int:photo_id>/', comment_photo, name='comment photo'),

)
