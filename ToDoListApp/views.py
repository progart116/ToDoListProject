from django.shortcuts import render
import django.urls
import django.views.decorators.http
import django.contrib.auth.decorators
import django.http
import ToDoListApp.models
import UserLogApp.models



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
    return render(request, "ToDoListApp/add_form.html")



@django.contrib.auth.decorators.login_required
@django.views.decorators.http.require_http_methods(["POST"])
def add_task_post(request):
    return django.http.HttpResponse("Not implemented: add post")



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
    return django.http.HttpResponse("Not implemented: complete post")
