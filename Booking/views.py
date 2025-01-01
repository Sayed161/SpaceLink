from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Room_Booking,Office_Booking,Desk_Booking
from datetime import datetime
from Office.models import Office, Room, Desk ,TimeSlot
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
# View for listing all bookings
@login_required
def booking_list(request):
    room_bookings = Room_Booking.objects.filter(user=request.user)
    office_bookings = Office_Booking.objects.filter(user=request.user)
    desk_bookings = Desk_Booking.objects.filter(user=request.user)

    bookings = list(room_bookings) + list(office_bookings) + list(desk_bookings)

    return render(request, 'booking_list.html', {'bookings': bookings})

@login_required
def book_desk(request, pk):
    desk = get_object_or_404(Desk, pk=pk)
    booking, created = Desk_Booking.objects.get_or_create(user=request.user, Desk=desk, booking_date= datetime.now().date())
    if created:
        messages.success(request, "Office has been booked successfully!")
    else:
        messages.info(request, "You have already booked this office today.")
    return redirect('list')

@login_required
def book_office(request, pk):
    office = get_object_or_404(Office, pk=pk)
    booking, created = Office_Booking.objects.get_or_create(user=request.user, office=office, booking_date= datetime.now().date())
    if created:
        messages.success(request, f"Office has booked successfully !")
    else:
        messages.info(request, "You have already booked this office today.")
    return redirect('list')

@login_required
def book_room(request, pk):
    room = get_object_or_404(TimeSlot, pk=pk)
    if request.method == 'POST':
        booking_date = datetime.now().date()
        booking, created = Room_Booking.objects.get_or_create(
            user=request.user, room=room, booking_date=booking_date
        )
        # Redirect or render success page after booking
        if created:
            messages.success(request, f"Office has booked successfully !")
        else:
            messages.info(request, "You have already booked this office today.")
    return redirect('list')
# View for canceling a booking
