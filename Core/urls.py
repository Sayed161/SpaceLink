from django.urls import path
from .views import home,office,room,desk_list,solutions,index


urlpatterns = [
    path('', home, name='home'),
    path('index/', index, name='index'),
    path('office/',office, name='office'),
    path('room/',room, name='room'),
    path('desk/',desk_list, name='desk'),
    path('solutions/',solutions, name='solution'),
]