from re import I
from django.db import models
import uuid
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save

# Create your models here.
class Account(models.Model):
    user = models.OneToOneField(to=User,on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    username = models.CharField(max_length=100, blank=False, null=False,unique=True)

    def __str__(self):
        return str(self.username)
    

