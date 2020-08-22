from django.db import models
from django.contrib.auth.models import User


class Vote(models.Model):
    start_user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.TextField('Заголовок', max_length=50)
    details = models.TextField('Детали')
    start_time = models.DateTimeField('Дата начала')

    def __str__(self):
        return f'{self.user.start_user.username} vote'


class Building(models.Model):
    city = models.TextField('Город')
    street = models.TextField('')