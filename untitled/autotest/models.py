from django.db import models
from django.contrib import admin
# Create your models here.



class User(models.Model):
    class Meta:
        db_table = 'user'
    #print('11')
    name = models.CharField(max_length=50, unique=True, null=False)
    password = models.CharField(max_length=10, unique=False,null=False)
    email = models.CharField(max_length=150, unique=True)
    tel = models.IntegerField()
    createtime = models.DateTimeField(max_length=50)

