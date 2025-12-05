from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.html import mark_safe
from django.utils.translation import gettext_lazy as _
# Create your models here.


class MCUserManager(BaseUserManager):
    use_in_migrations: bool = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueEurror("Email must be set")
        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def createuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a superuser with email and password"""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True")

        return self._create_user(email, password, **extra_fields)
    def get_by_natural_key(self, username):
        """
        Override this method to normalize the email input
        before attempting to find the user in the database.
        """
        email = self.normalize_email(username)
        return self.get(**{self.model.USERNAME_FIELD: email})

class MCUser(AbstractUser):
    email = models.EmailField(_("Email Address"), unique=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    profile_picture = models.ImageField(blank=True)
    username = None
    objects = MCUserManager()
    USERNAME_FIELD="email"
    REQUIRED_FIELDS=[]
    

    class Meta:
        ordering = ["email"]
        
