from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Custom user model with role-based access control."""

    class Role(models.TextChoices):
        PET_OWNER    = 'PET_OWNER', 'Pet Owner'
        STAFF        = 'STAFF', 'Staff'
        VETERINARIAN = 'VETERINARIAN', 'Veterinarian'
        BRANCH_ADMIN = 'BRANCH_ADMIN', 'Branch Admin'
        ADMIN        = 'ADMIN', 'Admin'

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.PET_OWNER,
    )
    branch = models.ForeignKey(
        'branches.Branch',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='users',
        help_text='The branch this user belongs to.',
    )
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True, help_text='Full address of the pet owner')

    # ── helper properties ──────────────────────────────────
    def is_admin_role(self):
        """Returns True for Admin and Branch Admin roles."""
        return self.role in (self.Role.ADMIN, self.Role.BRANCH_ADMIN)

    def is_clinic_staff(self):
        """Returns True for any role that accesses the admin portal."""
        return self.role in (
            self.Role.STAFF,
            self.Role.VETERINARIAN,
            self.Role.BRANCH_ADMIN,
            self.Role.ADMIN,
        )

    def is_pet_owner(self):
        return self.role == self.Role.PET_OWNER

    def save(self, *args, **kwargs):
        # Superusers should always have the ADMIN role
        if self.is_superuser and self.role == self.Role.PET_OWNER:
            self.role = self.Role.ADMIN
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['username']

    def __str__(self):
        return f'{self.username} ({self.get_role_display()})'
