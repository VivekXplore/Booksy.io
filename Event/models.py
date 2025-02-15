from django.db import models
from django.contrib.auth.models import User



class Feedback(models.Model):
    email=models.EmailField(max_length=200)
    name=models.CharField(max_length=30)
    suggestion=models.TextField(max_length=50)


def __str__(self):
    return f'{self.name} - {self.suggestion}'

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=50)
    date = models.DateField()
    time_slot = models.CharField(max_length=50)  # e.g., '9:00 AM - 12:00 PM'

    def __str__(self):
        return f"{self.event_type} - {self.date} ({self.time_slot})"
