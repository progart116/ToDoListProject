from django.shortcuts import render
import django.urls
import django.views.decorators.http
import django.contrib.auth.decorators
import django.http
import ToDoListApp.models
import UserLogApp.models
import datetime



@django.contrib.auth.decorators.login_required
def view_task_list(request):
    try:
        context = {
            "user": UserLogApp.models.User.objects.get(django_auth_user__username=str(request.user)),
            "tasks": ToDoListApp.models.Task.objects.filter(user__django_auth_user__username=str(request.user)),
        }
        UserLogApp.models.Logs.objects.create(log_data=f"Открыта страница отображения списка задач", app_name="ToDoListApp", method_name="views.view_task_list", program_user=str(request.user))
        return render(request, "ToDoListApp/list.html", context)
    except Exception as ex:
        UserLogApp.models.Logs.objects.create(log_data=f"Ошибка: {str(ex)}", app_name="ToDoListApp", method_name="views.view_task_list", program_user=str(request.user))
        return django.http.HttpResponseServerError()



@django.contrib.auth.decorators.login_required
def add_task_form(request):
    context = { "login": str(request.user) }
    UserLogApp.models.Logs.objects.create(log_data=f"Открыта страница добавления задачи", app_name="ToDoListApp", method_name="views.view_task_list", program_user=str(request.user))
    return render(request, "ToDoListApp/add_form.html", context)



@django.contrib.auth.decorators.login_required
@django.views.decorators.http.require_http_methods(["POST"])
def add_task_post(request):
    try:
        login = request.POST.get("login", None)
        name = request.POST.get("name", None)
        deadline_date = request.POST.get("deadline_date", None)
        deadline_time = request.POST.get("deadline_time", None)
        if login != str(request.user) or not UserLogApp.models.User.objects.filter(django_auth_user__username=login).exists(): return django.http.HttpResponseForbidden()
        if deadline_date == "": raise Exception("Не указана дата срока")
        if deadline_time == "": raise Exception("Не указано время срока")
        deadline = datetime.datetime(int(deadline_date[0:4]), int(deadline_date[5:7]), int(deadline_date[8:10]), int(deadline_time[0:2]), int(deadline_time[3:5]), 0)
        user = UserLogApp.models.User.objects.get(django_auth_user__username=login)
        new_task = ToDoListApp.models.Task.objects.create(user=user, name=name, deadline=deadline, completed=False)
        UserLogApp.models.Logs.objects.create(log_data=f"Добавлена задача {new_task.id}", app_name="ToDoListApp", method_name="views.add_task_post", program_user=str(request.user))
        return django.http.HttpResponseRedirect(django.urls.reverse("ToDoListApp:view_task_list"))
    except Exception as ex:
        context = { 
            "login": str(request.user),
            "error": f"Ошибка: {str(ex)}"
        }
        UserLogApp.models.Logs.objects.create(log_data=f"Ошибка при добавлении задачи: {str(ex)}. Повторно открыта страница добавления задачи", app_name="ToDoListApp", method_name="views.add_task_post", program_user=str(request.user))
        return render(request, "ToDoListApp/add_form.html", context)



@django.contrib.auth.decorators.login_required
def complete_task_post(request, id_task):
    try:
        task = ToDoListApp.models.Task.objects.get(id=id_task)
        if task.user.django_auth_user.username != str(request.user): return django.http.HttpResponseForbidden()
        else:
            task.completed = True
            task.save()
            UserLogApp.models.Logs.objects.create(log_data=f"Задача {task.id} завершена", app_name="ToDoListApp", method_name="views.complete_task_post", program_user=str(request.user))
            return django.http.HttpResponseRedirect(django.urls.reverse("ToDoListApp:view_task_list"))        
    except Exception as ex:
        UserLogApp.models.Logs.objects.create(log_data=f"Ошибка: {str(ex)}", app_name="ToDoListApp", method_name="views.complete_task_post", program_user=str(request.user))
        return django.http.HttpResponseServerError()
