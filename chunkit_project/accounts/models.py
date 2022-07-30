from datetime import datetime
from django.db import models

# Create your models here.


class chunkit_users(models.Model):
    password = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=20, null=True)
    email = models.EmailField(max_length=30, null=True)
    date_joined = models.DateTimeField(auto_now_add=True, null=True)
    is_active = models.SmallIntegerField(null=True)
    user_id = models.IntegerField(null=True)

    def __str__(self):
        return self.name

  
 
class authentication(models.Model):
    name = models.CharField(max_length=20, null=True)
    confirmed = models.SmallIntegerField(null=True)
    number = models.IntegerField(null=True)
    #connecting users table to authentication table
    #user_id = models.ForeignKey(chunkit_users, null=True, on_delete=models.CASCADE)
    key = models.CharField(max_length=100, null=True)
    user_id = models.ForeignKey(chunkit_users, null=True, on_delete=models.CASCADE)


    def __str__(self):
        return self.name


class Chunkedfile(models.Model):
    filename = models.CharField(max_length=20, null=True)
    filesize = models.IntegerField(null=True)
    filetype = models.CharField(max_length=100, null=True)
    owner_id = models.ManyToManyField(chunkit_users, null=True)
    date_chunked = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.filename

  