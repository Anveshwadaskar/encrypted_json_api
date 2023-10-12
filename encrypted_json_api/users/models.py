from django.db import models

# users/models.py
from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator, MaxLengthValidator, EmailValidator

class User(models.Model):
    username = models.CharField(max_length=12, unique=True, validators=[RegexValidator('^[A-Za-z0-9]*$', message='Only alphanumeric characters are allowed.'), MinLengthValidator(4), MaxLengthValidator(12)])
    password = models.CharField(max_length=128, validators=[MinLengthValidator(5), MaxLengthValidator(12), RegexValidator('^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]*$', message='Password must have one capital letter, one number, and one special character.')])
    mobile_number = models.PositiveIntegerField()
    address = models.TextField(max_length=120, blank=True, validators=[MaxLengthValidator(120)])
    email = models.EmailField(unique=True, validators=[EmailValidator()])
    is_active = models.BooleanField(default=True)

class LoginHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    login_time = models.DateTimeField(auto_now_add=True)
    logout_time = models.DateTimeField(null=True, blank=True)


# Create your models here.
