from django.db import models
from django.core.validators import MinLengthValidator

from petstagram.pets.models import Pet
from petstagram.photos.validators import max_file_size_validator_to_5MB


class PhotoModel(models.Model):
    LOCATION_MAX_LENGTH = 30
    DESCRIPTION_MAX_LENGTH = 300
    DESCRIPTION_MIN_LENGTH = 10

    photo = models.ImageField(
        upload_to='pet_photos/',
        validators=(max_file_size_validator_to_5MB,)
    )

    description = models.TextField(
        max_length=DESCRIPTION_MAX_LENGTH,
        validators=(MinLengthValidator(DESCRIPTION_MIN_LENGTH),),
        null=True,
        blank=True,
    )

    location = models.CharField(
        max_length=LOCATION_MAX_LENGTH,
        null=True,
        blank=True,
    )

    tagged_pets = models.ManyToManyField(Pet,
                                         blank=True,
                                         )

    date_of_publication = models.DateField(
        auto_now=True,
    )
