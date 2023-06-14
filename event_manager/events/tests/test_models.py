from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase
from django.utils import timezone
from datetime import timedelta
from events.models import Event, Category

User = get_user_model()


def create_user():
    return User.objects.create_user("john", "lennon@thebeatles.com", "johnpassword")


class TestEventModel(TestCase):
    """
    Testen des Event-Models
    """

    def setUp(self) -> None:
        """Wird vor jedem Test aufgerufen"""
        self.user = create_user()
        self.category = Category.objects.create(name="abc")
        self.date = timezone.now() + timedelta(hours=2)
        self.event = Event(
            name="Test Event",
            min_group=5,
            category=self.category,
            author=self.user,
            date=self.date,
        )

    def test_valid_event(self):
        """Unser erster Test"""
        self.event.save()
        is_event = Event.objects.filter(name="Test Event").exists()
        self.assertTrue(is_event)

    def test_invalid_date(self):
        """Unser erster Test"""
        self.event.date = timezone.now() - timedelta(hours=2)
        self.event.save()
        self.assertRaises(ValidationError, self.event.full_clean)
