from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class Pengguna(AbstractUser):
    nama_lengkap = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    is_admin = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        Group,
        related_name='pengguna_set',  # Mengganti related_name default
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        related_query_name='pengguna',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='pengguna_set',  # Mengganti related_name default
        blank=True,
        help_text=('Specific permissions for this user.'),
        related_query_name='pengguna',
    )

    def __str__(self):
        return self.username
