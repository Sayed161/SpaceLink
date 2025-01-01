from .views import book_desk, book_office, book_room,booking_list
from django.urls import path

urlpatterns = [
    path('list/',booking_list,name='list'),
    path('desk/book/<int:pk>/', book_desk, name='book-desk'),
    path('office/book/<int:pk>/', book_office, name='book-office'),
    path('room/book/<int:pk>/', book_room, name='book-room'),
]