from django.db import models


class UserType(models.Model):
    title = models.CharField(max_length=32)


class UserInfo(models.Model):
    name = models.CharField(max_length=16)
    age = models.IntegerField()
    ut = models.ForeignKey(UserType, on_delete=models.CASCADE)