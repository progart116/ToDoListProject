from django.contrib import admin
import UserLogApp.models

admin.site.register(UserLogApp.models.User)
admin.site.register(UserLogApp.models.Function)
admin.site.register(UserLogApp.models.AccessRights)

@admin.register(UserLogApp.models.Logs)
class Logs(admin.ModelAdmin):
    list_display = ['id', 'date', 'time', 'log_data', 'program_user']
    readonly_fields = ['id', 'date', 'time', 'log_data', 'app_name', 'method_name', 'program_version', 'program_user']

