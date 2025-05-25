from django.urls import path
import UserLogApp.views

app_name = "UserLogApp"

urlpatterns = [
    path('login/', UserLogApp.views.login_form, name="login_form"),
    path('login/post/', UserLogApp.views.login_post, name="login_post"),
    path('logout/', UserLogApp.views.logout_user, name="logout_user"),
    path('registration/', UserLogApp.views.registration_form, name="registration_form"),
    path('registration/post/', UserLogApp.views.registration_post, name="registration_post"),
    path('', UserLogApp.views.view_profile, name="view_profile"),
    path('change/password/', UserLogApp.views.change_password_form, name="change_password_form"),
    path('change/password/post/', UserLogApp.views.change_password_post, name="change_password_post"),
]