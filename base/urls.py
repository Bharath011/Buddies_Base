from django.urls import path
from . import views

urlpatterns=[
    path('login/',views.loginpage,name="login"),
    path('register/',views.registerpage,name="register"),
    path('',views.home,name="home"),
    path('room/<str:pk>/',views.room,name="room"),
    path('create-room/',views.createRoom,name="create-room"),
    path('update-room/<str:pk>/',views.updateRoom,name="update-room"),
    path('delete-room/<str:pk>/',views.deleteRoom,name="delete-room"),
    path('logout/',views.logoutuser,name="logout"),
    path('delete-message/<str:pk>/',views.deleteMessage,name="delete-message"),
    path('profile/<str:pk>/',views.userProfile,name="profile"),
    path('edit-user/',views.editUser,name="edit-user"),
    path('topics/',views.topicsPage,name="topics"),
    path('activity/',views.activityPage,name="activity")
]