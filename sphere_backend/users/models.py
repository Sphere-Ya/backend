from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """User model."""
    USER = 'user'
    ADMIN = 'administrator'
    ROLES = (
        (USER, 'user'),
        (ADMIN, 'administrator'),
    )
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(max_length=254, blank=False, unique=True)
    password = models.CharField(max_length=150, blank=False)
    role = models.CharField(max_length=16, choices=ROLES, default=USER)
    created_at = models.DateTimeField(verbose_name='Дата создания',
                                      auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
