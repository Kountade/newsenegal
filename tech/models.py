from django.db import models

# Create your models here.
from django.contrib.auth.models import User

# Create your models here.


class blog(models.Model):

    title = models.CharField(max_length=5000)
    description = models.TextField()
    image = models.ImageField()
    date = models.DateField(auto_now_add=True)
