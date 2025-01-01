from django import forms
from .models import Room_Booking,Desk_Booking,Office_Booking
from Account.models import User
from Office.models import Office, Room, Desk

class Room_BookingForm(forms.ModelForm):
    class Meta:
        model = Room_Booking
        fields = ['user','room', 'status']

    # Optional: You can add custom validations if needed
    def __init__(self, *args, **kwargs):
        super(Room_BookingForm, self).__init__(*args, **kwargs)

class Desk_BookingForm(forms.ModelForm):
    class Meta:
        model = Desk_Booking
        fields = ['user','Desk', 'status']

    # Optional: You can add custom validations if needed
    def __init__(self, *args, **kwargs):
        super(Desk_BookingForm, self).__init__(*args, **kwargs)


class Office_BookingForm(forms.ModelForm):
    class Meta:
        model = Office_Booking
        fields = ['user','office', 'status']

    # Optional: You can add custom validations if needed
    def __init__(self, *args, **kwargs):
        super(Office_BookingForm, self).__init__(*args, **kwargs)

