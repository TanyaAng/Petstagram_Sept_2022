from django.db import models

from petstagram.photos.models import PhotoModel


class Comment(models.Model):
    COMMENT_MAX_LENGTH = 300
    text = models.TextField(
        max_length=COMMENT_MAX_LENGTH,
    )

    date_time_of_publication = models.DateTimeField(auto_now_add=True, )

    to_photo = models.ForeignKey(PhotoModel, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date_time_of_publication']


class Like(models.Model):
    to_photo = models.ForeignKey(PhotoModel, on_delete=models.CASCADE)
