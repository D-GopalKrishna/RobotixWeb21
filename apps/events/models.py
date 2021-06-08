from django.db import models
from django.conf import settings
from django.utils.deconstruct import deconstructible
import os
import datetime as datetime
from time import strftime


User = settings.AUTH_USER_MODEL

RANK = (
    ("01","Rank 01"),
    ("02","Rank 02"),
    ("03","Rank 03"),
    ("PC","Participation")
)
EVENT_TYPE = (
    ("OO","ONLINE"),
    ("AB","ABSTRACT BASED"),
    ("PB","PITCHING BASED"),
    ("HT","HACKATHON"),
    ("WS","WORKSHOP"),
)
# Create your models here.

@deconstructible
class PathAndRename(object):
    def __init__(self, upload_to):
        self.upload_to = upload_to

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        now_time = datetime.datetime.now().strftime("%Y-%m-%d")
        filename = '{}.{}'.format(str(instance.rank) + '_' + str(now_time), ext)
        return os.path.join(self.upload_to, filename)


@deconstructible
class PathAndRename2(object):
    def __init__(self, upload_to):
        self.upload_to = upload_to

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        now_time = datetime.datetime.now().strftime("%Y-%m-%d")
        filename = '{}.{}'.format(str(instance.team_name) + '_' + str(now_time), ext)
        return os.path.join(self.upload_to, filename)




class CertImage(models.Model):
    rank=models.CharField(choices=RANK,max_length=2,null=True,blank=True)
    image=models.ImageField(upload_to=PathAndRename('event/Certificate/'),null=True,blank=True)
    
    def __str__(self):
        return self.event_name


class Event(models.Model):
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=1000)
    image = models.ManyToManyField(CertImage,blank=True)
    event_type = models.CharField(choices=EVENT_TYPE,max_length=2,blank=True,null=True)
    payment = models.IntegerField(null=True,blank=True)
    date_time = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.title

class Team(models.Model):
    team_name = models.CharField(max_length=150)
    email = models.EmailField()
    team_mates = models.ManyToManyField(User, related_name= "team_member")
    leader = models.OneToOneField(User, related_name= "admin",null=True, on_delete = models.CASCADE)
    selected = models.BooleanField(default=False,null=True)
    bid = models.IntegerField(default=0)
    mail_delivered = models.BooleanField(default=False)
    abstract = models.FileField(upload_to='event/docs/abstracts',null=True)
    image = models.ImageField(upload_to=PathAndRename2('event/docs/image'),null=True)
    college = models.CharField(max_length= 150, null= True)
    payment = models.BooleanField(default=False, null= True)

    def __str__(self):
        return self.team_name