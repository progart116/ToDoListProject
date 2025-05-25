from django.db import models
import UserLogApp.models

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(to=UserLogApp.models.User, verbose_name='Пользователь', on_delete=models.PROTECT)
    name = models.TextField('Название задачи')
    deadline = models.DateTimeField('Срок')
    copmpleted = models.BooleanField('Выполнено')

