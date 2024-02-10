from django.urls import path
from . import views 

urlpatterns =[
    path('login/',views.loginpage, name = "login"),
    path('logout/',views.logoutuser, name = "logout"),
    path('register/',views.registeruser, name = "register"),
    path('delete-message/<int:pk>/',views.deletemessage, name = "delete-message"),

    path('', views.home, name = "home"),
    path('room/<int:pk>/', views.room, name = "room"),
    path('create-room/',views.createroom, name = "create-room"),
    path('update-room/<int:pk>/',views.updateroom, name = "update-room"),
    path('delete-room/<int:pk>/',views.deleteroom, name = "delete-room"),

]