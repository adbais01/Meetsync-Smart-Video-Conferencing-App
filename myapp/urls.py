from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('meeting/', views.videocall, name='meeting'),
    path('logout/', views.logout_view, name='logout'),
    path('join/', views.join_room, name='join'),
    path('record-attendance/', views.record_attendance, name='record_attendance'),
    path('start-aircanvas/', views.trigger_aircanvas, name='start_aircanvas'),
    path("stop-aircanvas/", views.stop_aircanvas, name="stop_aircanvas"),

]