from django.db import models
from django.contrib.auth.models import AbstractUser # used to create a custom user model
from django.core import validators as v

# Create your models here.

class App_user(AbstractUser):
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField(default=18, validators=[v.MaxValueValidator(100), v.MinValueValidator(18)])
    display_name = models.CharField(default = 'unknown', max_length = 50)
    address = models.TextField(default = 'unknown')
    USERNAME_FIELD = 'email' # we are telling the user to use the email field as a username
    REQUIRED_FIELDS = []