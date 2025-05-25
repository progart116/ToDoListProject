from django.urls import path
import ToDoListApp.views

app_name = "ToDoListApp"

urlpatterns = [
    path('', ToDoListApp.views.view_task_list, name="login_form"),
    path('add/', ToDoListApp.views.add_task_form, name="add_task_form"),
    path('add/post/', ToDoListApp.views.add_task_post, name="add_task_post"),
    path('complete/<int:id_task>', ToDoListApp.views.complete_task_post, name="complete_task_post"),
]