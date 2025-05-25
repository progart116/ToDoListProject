from django.shortcuts import render
import django.views.decorators.http
import django.contrib.auth.decorators
import django.http



@django.contrib.auth.decorators.login_required
def view_task_list(request):
    return django.http.HttpResponse("Not implemented")



@django.contrib.auth.decorators.login_required
def add_task_form(request):
    return django.http.HttpResponse("Not implemented")



@django.contrib.auth.decorators.login_required
@django.views.decorators.http.require_http_methods(["POST"])
def add_task_post(request):
    return django.http.HttpResponse("Not implemented")



@django.contrib.auth.decorators.login_required
@django.views.decorators.http.require_http_methods(["POST"])
def complete_task_post(request, id_task):
    return django.http.HttpResponse("Not implemented")
