from django.shortcuts import render
import django.views.decorators.http
import django.contrib.auth.decorators
import django.http
import UserLogApp.models



def login_form(request):
    return django.http.HttpResponse("Not implemented")



@django.views.decorators.http.require_http_methods(["POST"])
def login_post(request):
    return django.http.HttpResponse("Not implemented")



def logout_user(request):
    return django.http.HttpResponse("Not implemented")



def registration_form(request):
    return django.http.HttpResponse("Not implemented")



@django.views.decorators.http.require_http_methods(["POST"])
def registration_post(request):
    return django.http.HttpResponse("Not implemented")



@django.contrib.auth.decorators.login_required
def view_profile(request):
    return django.http.HttpResponse("Not implemented")



@django.contrib.auth.decorators.login_required
def change_password_form(request):
    return django.http.HttpResponse("Not implemented")



@django.contrib.auth.decorators.login_required
@django.views.decorators.http.require_http_methods(["POST"])
def change_password_post(request):
    return django.http.HttpResponse("Not implemented")



