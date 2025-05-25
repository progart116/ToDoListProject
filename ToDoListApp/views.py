from django.shortcuts import render
import django.views.decorators.http
import django.contrib.auth.decorators
import django.http
import ToDoListApp.models



@django.contrib.auth.decorators.login_required
def view_task_list(request):
    return render(request, "ToDoListApp/list.html")



@django.contrib.auth.decorators.login_required
def add_task_form(request):
    return render(request, "ToDoListApp/add_form.html")



@django.contrib.auth.decorators.login_required
@django.views.decorators.http.require_http_methods(["POST"])
def add_task_post(request):
    return django.http.HttpResponse("Not implemented: add post")



@django.contrib.auth.decorators.login_required
@django.views.decorators.http.require_http_methods(["POST"])
def complete_task_post(request, id_task):
    return django.http.HttpResponse("Not implemented: complete post")
