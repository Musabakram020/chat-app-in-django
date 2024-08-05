from django.urls import path,include
from . import views
urlpatterns = [

    path('', views.lobby,name ='lobby'),
    path('room/', views.rooms,name='rooms'),
    path('get_token/', views.getToken),
    path('create_member/',views.createUser),
    path('get_member/',views.getMember),
    path('delete_member/',views.deleteUser)
]
