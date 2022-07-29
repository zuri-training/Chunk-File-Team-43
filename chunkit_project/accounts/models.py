from datetime import datetime
from django.db import models

# Create your models here.


class accounts(models.Model):
    password = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=20, null=True)
    email = models.EmailField(max_length=30, null=True)
    date_joined = models.DateTimeField(auto_now_add=True, null=True)
    is_active = models.SmallIntegerField(null=True)
    user_id = models.IntegerField(null=True)
  
 
class authentication(models.Model):
    name = models.CharField(max_length=20, null=True)
    confirmed = models.SmallIntegerField(null=True)
    number = models.IntegerField(null=True)
    user_id = models.IntegerField(null=True)
    key = models.CharField(max_length=100, null=True)

class Chunkedfile(models.Model):
    filename = models.CharField(max_length=20, null=True)
    filesize = models.IntegerField(null=True)
    filetype = models.CharField(max_length=100, null=True)
    owner_id = models.IntegerField(null=True)
    date_chunked = models.DateTimeField(auto_now_add=True, null=True)

  