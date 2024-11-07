from django.test import TestCase
from .models import Event, Category, RSVP
from accounts.models import User

class EventTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.category = Category.objects.create(name='Test Category')
        self.event = Event.objects.create(
            title='Test Event',
            description='This is a test event',
            date='2023-12-31 23:59:59',
            location='Test Location',
            organizer=self.user,
            category=self.category,
            max_capacity=100
        )

    def test_event_creation(self):
        self.assertEqual(self.event.title, 'Test Event')
        self.assertEqual(self.event.organizer, self.user)