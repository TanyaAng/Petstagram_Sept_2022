from enum import Enum

from django.core import validators
from django.db import models
from django.contrib.auth import models as auth_models

from petstagram.core.model_mixins import ChoiceEnumMixin
from petstagram.core.validators import only_letters_validator


class Gender(ChoiceEnumMixin, Enum):
    male = 'Male'
    female = 'Female'
    DoNotShow = 'Do not show'


class PetstagramUser(auth_models.AbstractUser):
    FIRST_NAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 30

    email = models.EmailField(
        unique=True,
    )

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(validators.MinLengthValidator(FIRST_NAME_MIN_LENGTH),
                    only_letters_validator,
                    )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(validators.MinLengthValidator(LAST_NAME_MIN_LENGTH),
                    only_letters_validator,)
    )

    profile_picture = models.URLField()

    gender = models.CharField(
        max_length=Gender.max_len(),
        choices=Gender.choices(),
    )

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        elif self.first_name or self.last_name:
            return self.first_name or self.last_name
