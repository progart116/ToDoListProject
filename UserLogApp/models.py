from django.db import models
import django.contrib.auth.models
import ToDoListProject.settings

class User(models.Model):
    id = models.AutoField(primary_key=True)
    django_auth_user = models.OneToOneField(to=django.contrib.auth.models.User, verbose_name='Пользователь Django', on_delete=models.PROTECT)
    surname = models.CharField('Фамилия', max_length=150, null=True, blank=True)
    firstname = models.CharField('Имя', max_length=150, null=True, blank=True)
    secondname = models.CharField('Отчество', max_length=150, null=True, blank=True)
    email = models.CharField('Адрес электронной почты', max_length=150, null=True, blank=True)
    is_active = models.BooleanField('Активный')
    reason_locked = models.CharField('Причина блокировки', max_length=150, null=True, blank=True)
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f"{self.id}. {self.surname} {self.firstname} {self.secondname} ({self.django_auth_user.username})"
    
    def get_full_name(self):
        try: return f"{self.surname} {self.firstname[0]}.{self.secondname[0]}."
        except: return self.django_auth_user.username



class Logs(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField('Дата события', auto_now=True)
    time = models.TimeField('Время события', auto_now=True)
    log_data = models.TextField('Событие')
    app_name = models.CharField('Наименование приложения', max_length=150)
    method_name = models.CharField('Наименование метода', max_length=150)
    program_version = models.CharField('Версия ПО', max_length=150, default=ToDoListProject.settings.PROGRAM_VERSION)
    program_user = models.CharField('Имя пользователя', max_length=150)

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'Журнал событий'

    def __str__(self):
        return f"{self.id}. {self.log_data}"



class Function(models.Model):
    id = models.AutoField(primary_key=True)
    code_name = models.CharField('Кодовое наименование функции', max_length=150)
    full_name = models.CharField('Полное наименование функции', max_length=150, null=True, blank=True)
    description = models.TextField('Описание функции', null=True, blank=True)

    class Meta:
        verbose_name = 'Функция ПО'
        verbose_name_plural = 'Функции ПО'

    def __str__(self):
        return self.code_name



class AccessRights(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField('Дата предоставления права', auto_now=True)
    time = models.TimeField('Время предоставления права', auto_now=True)
    user = models.ForeignKey(to=User, related_name='user', verbose_name='Пользователь', on_delete=models.PROTECT)
    function = models.ForeignKey(to=Function, verbose_name='Функция ПО', on_delete=models.PROTECT)
    access = models.BooleanField('Разрешено')
    initiator = models.ForeignKey(to=User, related_name='initiator', verbose_name='Инициатор', on_delete=models.PROTECT)
    reason = models.CharField('Причина предоставления/отзыва права', max_length=150, null=True, blank=True)
    
    class Meta:
        verbose_name = 'Право пользователя'
        verbose_name_plural = 'Права пользователей'

    def __str__(self):
        return f"{self.id}. Для сотрудника {self.user.django_auth_user.username} действие {self.function.code_name} разрешено: {self.allow}"

