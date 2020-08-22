from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Vote(models.Model):
    start_user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField('Заголовок', max_length=50)
    details = models.TextField('Детали')
    start_time = models.DateTimeField('Дата начала', default=datetime.now, blank=True)

    def __str__(self):
        return f'{self.title} vote'

"""
class Building(models.Model):
    city = models.TextField('Город')
    street = models.TextField('')
"""