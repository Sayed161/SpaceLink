from django.db import models
from Company.models import Company,OfficeAmenities
# Create your models here.
class Office(models.Model):
    office_name = models.CharField(max_length=200)
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    time = models.CharField(max_length=400)
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    Cancellation_policy=models.CharField(max_length=600)
    Guest_policy=models.CharField(max_length=600)
    capacity = models.IntegerField(default=0)
    image = models.ImageField(upload_to='offices/')

    def __str__(self):
        return self.office_name


class Room(models.Model):
    room_name = models.CharField(max_length=200)
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    capacity = models.IntegerField(default=0)
    amenities = models.ManyToManyField(OfficeAmenities)
    image = models.ImageField(upload_to='room_images/')

    def __str__(self):
        return self.room_name
class TimeSlot(models.Model):
    Room=models.ForeignKey(Room,on_delete=models.CASCADE,null=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    price = models.DecimalField(max_digits=6,decimal_places=2)
    is_booked = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.Room.room_name}-{self.start_time} and {self.end_time}"
class Desk(models.Model):
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    time = models.CharField(max_length=400)
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    Cancellation_policy=models.CharField(max_length=600)
    Guest_policy=models.CharField(max_length=600)
    desk = models.IntegerField(default=0)
    image = models.ImageField(upload_to='desk/')

    def __str__(self):
        return f'{self.company } has {self.desk}'