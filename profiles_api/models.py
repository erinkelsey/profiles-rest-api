from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """Create a new user profile

        Args:
            email (str): email for new user. Cannot be None.
            name (str): name of new user.
            password (str, optional): password for new user. Defaults to None.

        Raises:
            ValueError: when an email is not specified

        Returns:
            User: the new user created
        """
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create a new super user

        Args:
            email (str): email for new user. Cannot be None.
            name (str): name of new user.
            password (str, optional): password for new user. Defaults to None.

        Raises:
            ValueError: when an email is not specified

        Returns:
            User: the new user created
        """
        user = self.create_user(email, name, password)
        user.is_superuser = True 
        user.is_staff = True 
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=25, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name 

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name 

    class Meta:
        """Meta definition for UserProfile."""

        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'

    def __str__(self):
        """Unicode representation of UserProfile."""
        return self.email

