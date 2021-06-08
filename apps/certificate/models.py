#models
from django.db import models
import uuid
from events.models import Event
#signals
from django.dispatch import receiver
from django.db.models.signals import post_delete
from django.utils.deconstruct import deconstructible
import os
import datetime as datetime
from time import strftime


# Create your models here.'

@deconstructible
class PathAndRename(object):
    def __init__(self, upload_to):
        self.upload_to = upload_to

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        now_time = datetime.datetime.now().strftime("%Y-%m-%d")
        filename = '{}.{}'.format(str(instance.name) + '_' + str(now_time), ext)
        return os.path.join(self.upload_to, filename)


class Certificate(models.Model):
    event = models.ForeignKey(Event,related_name='events',on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    url_key = models.UUIDField(default=uuid.uuid4,unique=True, blank=True,  null=True)
    image = models.ImageField(upload_to=PathAndRename('certificate/'),null=True,blank=True)
    email = models.EmailField(null=True)
    image_created = models.BooleanField(default=False,null=True)
    email_sent = models.BooleanField(default=False,null=True)

    def __str__(self):
        return self.name + " certificate for event " + self.event.title


@receiver(post_delete, sender=Certificate)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
