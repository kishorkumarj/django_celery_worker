from django.db import models
from django.contrib.auth.models import AbstractUser
from .constants import USER_ROLE_COHICES, USER

# Create your models here.

class User(AbstractUser):
    username = None
    email = models.EmailField(max_length=100, unique=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    middle_name = models.CharField(max_length=50, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    
    @classmethod
    def create_user(cls, email, password, **kwargs):
        if not email:
            raise ValueError("Missing email")

        #email = self.normalize_username(email)
        user = cls(email=email, **kwargs)
        user.set_password(password)
        user.save()

        return user

    @classmethod
    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_active', True)

        return self.create_user(email, password, **kwargs)
    
    @property
    def user_roles(self):
        return [item.role for item in self.roles]

    def add_user_role(self, roles):
        for role in roles:
            self.roles.get_or_create(role=role)

    def has_permission(self, role):
        return self.roles.filter(role=role).count > 0

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=20, null=True, blank=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.email
    
class UserRoles(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='roles')
    role = models.CharField(max_length=20,choices=USER_ROLE_COHICES, default=USER)

    def __str__(self):
        return "{0} - [{1}]".format(self.user.email, self.role)
