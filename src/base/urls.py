from django.urls import path
from . views import rooms_views,create_room,update_room,delete_room,loginPage,logoutUser,registerUser,delete_message,UserProfile,updateUser

app_name='base'

urlpatterns = [
    path('login/',loginPage,name='login'),
    path('logout',logoutUser,name='logout'),
    path('register/',registerUser,name='register'),
    path('profile/<str:pk>/',UserProfile,name='profile'),

    path('rooms/<str:pk>', rooms_views, name='rooms'),
    path('create-room/', create_room, name='create'),
    path('update-room/<str:pk>', update_room, name='update'),
    path('delete-room/<str:pk>', delete_room, name='delete'),
    path('delete-message/<str:pk>', delete_message, name='delete-message'),
    path('update-user/', updateUser, name='update-user'),
    
]