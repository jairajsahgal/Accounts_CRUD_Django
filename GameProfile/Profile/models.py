from django.db import models
import uuid

# Create your models here.
class Account(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    username = models.CharField(max_length=100, blank=False, null=False,unique=True)

    def __str__(self):
        return str(self.username)