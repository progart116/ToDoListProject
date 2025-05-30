from django.shortcuts import render
import django.views.decorators.http
import django.contrib.auth.decorators
import django.http
import UserLogApp.models
import django.contrib.auth
import django.contrib.auth.models
import django.contrib.auth.hashers
import django.urls



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
    try:
        if request.user.is_authenticated: django.contrib.auth.logout(request)
        user_login = request.POST['login']
        user_password = request.POST['password']
        user_by_login = UserLogApp.models.User.objects.filter(django_auth_user__username=user_login)

        if user_by_login.exists():
        
            user_by_login = UserLogApp.models.User.objects.get(django_auth_user__username=user_login)
            if not user_by_login.is_active:
                context = { 
                    "error": "Пользовтель заблокирован!", 
                    "decorator_redirect": request.POST['decorator_redirect'], 
                    "user_list": UserLogApp.models.User.objects.filter(is_active=True) 
                }
                UserLogApp.models.Logs.objects.create(log_data=f"Попытка входа заблокированного пользователя. Пользователь {user_by_login.django_auth_user.username}. Причина блокировки: {user_by_login.reason_locked}. Повторно открыта страница аутентификации", app_name="UserLogApp", method_name="views.login_post", program_user=str(request.user))
                return render(request, "UserLogApp/login_form.html", context)
            authenticate_user = django.contrib.auth.authenticate(request, username=user_login, password=user_password)
        
            if authenticate_user:
                django.contrib.auth.login(request, authenticate_user)
                UserLogApp.models.Logs.objects.create(log_data=f"Пользователь {user_by_login.django_auth_user.username} вошел в систему", app_name="UserLogApp", method_name="views.login_post", program_user=str(request.user))
                return django.http.HttpResponseRedirect(request.POST['decorator_redirect'])
        
            else:
                context = { 
                    "error": "Неверный пароль!", 
                    "decorator_redirect": request.POST['decorator_redirect'], 
                    "user_list": UserLogApp.models.User.objects.filter(is_active=True) 
                }
                UserLogApp.models.Logs.objects.create(log_data=f"Пользователь {user_by_login.django_auth_user.username} ввел неверный пароль. Повторно открыта страница аутентификации", app_name="UserLogApp", method_name="views.login_post", program_user=str(request.user))
                return render(request, "UserLogApp/login_form.html", context)
        
        else:
            context = { 
                    "error": "Пользователь не найден!", 
                    "decorator_redirect": request.POST['decorator_redirect'], 
                    "user_list": UserLogApp.models.User.objects.filter(is_active=True) 
                }
            UserLogApp.models.Logs.objects.create(log_data=f"Пользователь {user_login} не найден. Повторно открыта страница аутентификации", app_name="UserLogApp", method_name="views.login_post", program_user=str(request.user)) 
            return render(request, "UserLogApp/login_form.html", context)
    
    except Exception as ex:
        UserLogApp.models.Logs.objects.create(log_data=f"Ошибка: {str(ex)}", app_name="UserLogApp", method_name="views.login_post", program_user=str(request.user))
        raise django.http.HttpResponseServerError()



def logout_user(request):
    UserLogApp.models.Logs.objects.create(log_data=f"Пользователь {str(request.user)} вышел из системы", app_name="UserLogApp", method_name="views.logout_user", program_user=str(request.user))
    if request.user.is_authenticated: django.contrib.auth.logout(request)
    return django.http.HttpResponseRedirect(django.urls.reverse("UserLogApp:login_form"))



def registration_form(request):
    return render(request, "UserLogApp/registration_form.html")



@django.views.decorators.http.require_http_methods(["POST"])
def registration_post(request):
    try:
        login = request.POST.get("login", None)
        password = request.POST.get("password", None)
        surname = request.POST.get("surname", None)
        firstname = request.POST.get("firstname", None)
        secondname = request.POST.get("secondname", None)
        email = request.POST.get("email", None)
        if login=="": raise Exception("Пустой логин")
        if password=="": raise Exception("Пустой пароль")
        if django.contrib.auth.models.User.objects.filter(username=login).exists(): raise Exception("Пользователь с таким логином уже существует")
        django_auth_user = django.contrib.auth.models.User.objects.create_user(username=login, password=password)
        UserLogApp.models.User.objects.create(django_auth_user=django_auth_user, surname=surname, firstname=firstname, secondname=secondname, email=email, is_active=True)
        return django.http.HttpResponseRedirect(django.urls.reverse("UserLogApp:login_form"))
    except Exception as ex:
        context = { "error": f"Ошибка: {str(ex)}" }
        return render(request, "UserLogApp/registration_form.html", context)



@django.contrib.auth.decorators.login_required
def view_profile(request):
    context = { "user": UserLogApp.models.User.objects.get(django_auth_user__username=str(request.user)) }
    return render(request, "UserLogApp/profile.html", context)



@django.contrib.auth.decorators.login_required
def change_password_form(request):
    context = { "user": UserLogApp.models.User.objects.get(django_auth_user__username=str(request.user)) }
    return render(request, "UserLogApp/change_password_form.html", context)



@django.contrib.auth.decorators.login_required
@django.views.decorators.http.require_http_methods(["POST"])
def change_password_post(request):
    try:
        login = request.POST.get("login", None)
        old_password = request.POST.get("old_password", None)
        new_password = request.POST.get("new_password", None)
        if login != str(request.user) or not UserLogApp.models.User.objects.filter(django_auth_user__username=login).exists(): return django.http.HttpResponseForbidden()
        django_auth_user = django.contrib.auth.models.User.objects.get(username=login)
        if not django.contrib.auth.hashers.check_password(old_password, django_auth_user.password): raise Exception("Некорректный старый пароль")
        if len(new_password) < 1: raise Exception("Новый пароль не введен")
        UserLogApp.models.Logs.objects.create(log_data=f"Пользователь {django_auth_user.username} сменил пароль", app_name="UserLogApp", method_name="views.change_password_post", program_user=str(request.user))
        django_auth_user.set_password(new_password)
        django_auth_user.save()
        django.contrib.auth.logout(request)
        authenticate_user = django.contrib.auth.authenticate(request, username=login, password=new_password)
        django.contrib.auth.login(request, authenticate_user)
        return django.http.HttpResponseRedirect(django.urls.reverse("UserLogApp:view_profile"))
    except Exception as ex:
        context = { 
            "user": UserLogApp.models.User.objects.get(django_auth_user__username=str(request.user)),
            "error": f"Ошибка: {str(ex)}" 
        }
        return render(request, "UserLogApp/change_password_form.html", context)



