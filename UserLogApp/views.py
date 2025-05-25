from django.shortcuts import render
import django.views.decorators.http
import django.contrib.auth.decorators
import django.http
import UserLogApp.models



def login_form(request):
    try:
        if request.user.is_authenticated: return django.http.HttpResponseRedirect(django.urls.reverse("ToDoListApp:view_task_list"))
        else:
            context = { 
                "decorator_redirect": request.GET.get("next", django.urls.reverse("ToDoListApp:view_task_list")), 
                "user_list": UserLogApp.models.User.objects.filter(is_active=True) 
            }
            UserLogApp.models.Logs.objects.create(log_data="Открыта страница аутентификации", app_name="UserLogApp", method_name="views.login_form", program_user=str(request.user))
            return render(request, "UserLogApp/login_form.html", context)
    except Exception as ex:
        UserLogApp.models.Logs.objects.create(log_data=f"Ошибка: {str(ex)}", app_name="UserLogApp", method_name="views.login_form", program_user=str(request.user))
        raise django.http.HttpResponseServerError()



@django.views.decorators.http.require_http_methods(["POST"])
def login_post(request):
    return django.http.HttpResponse("Not implemented: login post")



def logout_user(request):
    return django.http.HttpResponse("Not implemented: logout")



def registration_form(request):
    return render(request, "UserLogApp/registration_form.html")



@django.views.decorators.http.require_http_methods(["POST"])
def registration_post(request):
    return django.http.HttpResponse("Not implemented: reg post")



@django.contrib.auth.decorators.login_required
def view_profile(request):
    return render(request, "UserLogApp/profile.html")



@django.contrib.auth.decorators.login_required
def change_password_form(request):
    return render(request, "UserLogApp/change_password_form.html")



@django.contrib.auth.decorators.login_required
@django.views.decorators.http.require_http_methods(["POST"])
def change_password_post(request):
    return django.http.HttpResponse("Not implemented: chpwd post")



