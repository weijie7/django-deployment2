from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, models.SET_NULL, null = True)

    #PORTFOLIO
    portfolio_site = models.URLField(blank=True)
    profile_pic= models.ImageField(upload_to = 'profile_pics', blank=True)
    def __str__(self):
        return self.user.username


class Topic(models.Model):
    top_name = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    topic = models.ForeignKey(Topic,models.SET_NULL, null = True)
    name = models.CharField(max_length = 264, unique = True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage,models.SET_NULL, null = True)
    date = models.DateField()

    def __str__(self):
        return str(self.date)
