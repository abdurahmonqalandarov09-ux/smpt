
from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('confirm-email/', views.confirm_email, name='confirm_email'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.show_profile, name='profile'),
    path('tasks/', views.show_tasks, name='show_tasks'),
    path('tasks/create/', views.create_task, name='create_task'),
    path('tasks/update/<int:id>/', views.update_task, name='update_task'),
    path('tasks/delete/<int:id>/', views.delete_task, name='delete_task'),
]
