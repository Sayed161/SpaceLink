from django.contrib import admin
from .models import Room_Booking,Desk_Booking,Office_Booking
# Register your models here.
admin.site.register(Room_Booking)
admin.site.register(Desk_Booking)
admin.site.register(Office_Booking)