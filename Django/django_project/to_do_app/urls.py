from django.urls import path
from .views import home, add_to_do , show_update,update, delete 
urlpatterns = [
    path('home/', home, name='home'),
    path('add_todo/',add_to_do, name="add_todo"),
    path('update_todo/<int:todo_id>',show_update, name='update_todo'),
    path('update/<int:todo_id>',update, name='update'),
    path('delete/<int:todo_id>',delete, name='delete'),
]