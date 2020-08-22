from django.db import models


class User(models.Model):
    status = models.IntegerField(default='0')

    login = models.CharField(max_length=20)
    password = models.CharField(max_length=32)

    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)

    numberRequestEGRN = models.IntegerField()



