from django.db import models
from accounts.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='events')
    max_capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.title
    
    
class RSVP(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='rsvps')
    attendee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rsvps')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.attendee.username} RSVPed for {self.event.title}"