from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance=None,created=False,**kwargs):
    if created:
        Token.objects.create(user=instance)


def photos_directory(instance,filename):
    return "photo/{user_id}/{uuid}_{filename}".format(user_id=instance.user.id,uuid=str(uuid1()),filename=filename)


class Photo(models.Model):
    user = models.ForeignKey(User)
    photo= models.ImageField(upload_to="photos/", null=True ,blank=True)
    like= models.IntegerField(default=0)
    def __str__(self):
        return str(self.id)

class Comment(models.Model):
    user = models.ForeignKey(User)
    photo = models.ForeignKey(Photo)
    comment = models.TextField()
    def __str__(self):
        return "{0} - {1}".format(self.user.username,self.comment)