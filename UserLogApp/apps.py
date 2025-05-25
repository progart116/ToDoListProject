from django.apps import AppConfig


class UserlogappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'UserLogApp'
    verbose_name = 'Журнал событий и расширенные данные для пользователей'
