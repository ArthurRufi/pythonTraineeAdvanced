from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    password = models.CharField()
    lastlogin = models.DateTimeField()
    email = models.EmailField()
    oldpassword = models.CharField()
    emailHelp = models.EmailField()
    pass