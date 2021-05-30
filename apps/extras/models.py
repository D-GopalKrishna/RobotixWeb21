from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.

class DIY_FYI(models.Model):
    title = models.CharField(max_length=50, null= True, blank= True)
    desc = models.CharField(max_length=1000, null= True, blank= True)
    image = models.ImageField(upload_to='extras/diy_fyi/img', null= True, blank= True)
    mentor = models.CharField(max_length=50, null= True, blank= True)
    members = ArrayField(models.CharField(max_length=10, blank=True),size=8, null= True, blank= True)
    link = models.URLField(null= True, blank= True)
    file = models.FileField(upload_to='extras/diy_fyi/docs', null= True, blank= True)

    def __str__(self):
        return self.title


class Sponsors(models.Model):
    name = models.CharField(max_length= 150, null= True, blank= True)
    sponsor_type = models.CharField(max_length= 150, null= True, blank= True)
    website = models.CharField(max_length= 150, null= True, blank= True)
    phone_number = models.IntegerField(null= True, blank= True)
    logo = models.FileField(null= True, blank= True,upload_to='extras/sponsors')

    def __str__(self):
        return self.name


class Web(models.Model):
    img = models.ImageField(upload_to='extras/webteam',default='')
    name = models.CharField(max_length=200)
    branch = models.CharField(max_length=50)
    linkedin = models.URLField()
    email = models.EmailField()
    phone = models.CharField(max_length=13)

    def __str__(self):
        return self.name


class Emails(models.Model):
    email = models.EmailField(max_length=254)
    verified = models.BooleanField(default=False)


class Gallery(models.Model):
    photo = models.ImageField(upload_to='extras/gallery')
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=500)

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=110)
    email = models.EmailField()
    message = models.CharField(max_length=5000)
    time = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name