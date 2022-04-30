from django.db.models.signals import pre_save, post_save
from .models import Account, User


def set_username(sender, instance, created, **kwargs):
    print(instance)
    if created==True:
        account = instance
        u=User.objects.create(username=account.username)
        u.save()
        account.user=User.objects.get(username=account.username)
        print(account,"\t",account.user)


post_save.connect(set_username,sender=Account)