from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('resources/', views.resources, name="resources"),
    path('loginscreen/', views.loginscreen, name='loginscreen'),
    path('join/', views.join, name='join'),
    path('new_event/', views.new_event_page, name='new_event'),
    path('update_event/', views.update_event, name="update_event"),
    path('attendance_page/', views.attendance_page, name="attendance_page"), 
    path('mark_attendance/', views.mark_attendance, name="mark_attendance"),
    path('make_user_page', views.makeUserPage, name="make_user_page"),
    path('create_user', views.createUser, name="createUser")
]