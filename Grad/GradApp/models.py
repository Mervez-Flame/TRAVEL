from django.db import models

# Create your models here 
class Flight(models.Model):
    flight_number = models.CharField(max_length=10)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_date = models.DateTimeField()
    arrival_date = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bookings = models.IntegerField(default=0)
    slot_left = models.IntegerField(default=0)
    is_cancelled = models.BooleanField(default=False)

    #def __str__(self):
        #return f"{self.flight_number} - {self.origin} to {self.destination}"

class Booking(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger_name = models.CharField(max_length=100)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=15)
    num_passengers = models.PositiveIntegerField()
    booking_date = models.DateTimeField(auto_now_add=True)

    #def __str__(self):
        #return f"{self.passenger_name} - {self.flight}"
