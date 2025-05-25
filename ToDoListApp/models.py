from django.db import models
import UserLogApp.models

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(to=UserLogApp.models.User, verbose_name='Пользователь', on_delete=models.PROTECT)
    name = models.TextField('Название задачи')
    deadline = models.DateTimeField('Срок')
    completed = models.BooleanField('Выполнено')

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return f"{self.id}. {self.name} для пользователя {self.user.django_auth_user.username}"
    
    def verbose_completed(self):
        if self.completed: return "Да"
        else: return "Нет"

    def get_full_deadline(self):
        day = str(self.deadline.day)
        month = str(self.deadline.month)
        year = str(self.deadline.year)
        hour = str(self.deadline.hour)
        minute = str(self.deadline.minute)
        second = str(self.deadline.second)

        if len(day) == 1: day = f"0{day}"
        if len(month) == 1: month = f"0{month}"
        if len(hour) == 1: hour = f"0{hour}"
        if len(minute) == 1: minute = f"0{minute}"
        if len(second) == 1: second = f"0{second}"

        return f"{day}.{month}.{year} {hour}:{minute}:{second}"

