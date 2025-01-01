from django.db import models
from Account.models import User
from Office.models import Office, TimeSlot, Desk  # Ensure this imports correctly

class Room_Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(TimeSlot, null=True, blank=True, on_delete=models.CASCADE)
    booking_date = models.DateField()
    
    status_choices = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('canceled', 'Canceled'),
    ]
    status = models.CharField(max_length=10, choices=status_choices, default='pending')

    def __str__(self):
        return f"Booking {self.id} for {self.user.email} on {self.booking_date}"


class Desk_Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Desk = models.ForeignKey(Desk, null=True, blank=True, on_delete=models.CASCADE)
    booking_date = models.DateField()
    
    status_choices = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('canceled', 'Canceled'),
    ]
    status = models.CharField(max_length=10, choices=status_choices, default='pending')

    def __str__(self):
        return f"Booking {self.id} for {self.user.email} on {self.booking_date}"
    
class Office_Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    office = models.ForeignKey(Office, null=True, blank=True, on_delete=models.CASCADE)
    booking_date = models.DateField()
    
    status_choices = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('canceled', 'Canceled'),
    ]
    status = models.CharField(max_length=10, choices=status_choices, default='pending')

    def __str__(self):
        return f"Booking {self.id} for {self.user.email} on {self.booking_date}"