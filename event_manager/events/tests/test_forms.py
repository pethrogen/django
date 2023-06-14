from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.utils import timezone
from django.urls import reverse
from datetime import timedelta
from events.models import Event, Category

User = get_user_model()


def create_user(username):
    return User.objects.create_user(username, f"{username}@the.com", "johnpassword")


class TestEventForm(TestCase):
    """
    Testen des Event Formulars
    """

    def setUp(self) -> None:
        """Wird vor jedem Test aufgerufen"""
        self.user = create_user("john")
        self.client = Client()
        self.client.force_login(self.user)
        self.category = Category.objects.create(name="abc")
        self.date = timezone.now() + timedelta(hours=2)

        self.payload = {
            "name": "ein Test Name",
            "sub_title": "ein subtitle",
            "category": self.category.pk,
            "min_group": 5,
            "date": self.date,
        }

    def test_valid_input(self):
        """Testen, ob ein EVent mit validem Input angelegt werden kann."""
        response = self.client.post(reverse("events:event_create"), data=self.payload)
        is_event = Event.objects.filter(name=self.payload["name"]).exists()

        self.assertEqual(response.status_code, 302)
        self.assertTrue(is_event)

    def test_invalid_user(self):
        """Testen, ob nicht authetifizierter User Event anlegen kann"""
        client = Client()
        response = client.post(reverse("events:event_create"), data=self.payload)
        self.assertEqual(response.status_code, 302)
        is_event = Event.objects.filter(name=self.payload["name"]).exists()
        self.assertFalse(is_event)

    def test_wrong_author(self):
        """Testen, ob User einen anderen Event updaten kann."""
        response = self.client.post(reverse("events:event_create"), data=self.payload)
        event = Event.objects.get(name=self.payload["name"])

        user = create_user("bob")
        client = Client()
        client.force_login(user)

        self.payload["name"] = "FAKED"

        response = client.post(
            reverse("events:event_update", args=(event.pk,)), data=self.payload
        )

        is_event = Event.objects.filter(name=self.payload["name"]).exists()
        self.assertFalse(is_event)
        self.assertEqual(response.status_code, 403)
