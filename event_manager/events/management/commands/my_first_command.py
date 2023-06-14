from django.core.management.base import BaseCommand, CommandParser
from events.models import Event


class Command(BaseCommand):
    def add_arguments(self, parser) -> None:
        parser.description = "Erstelle Report alle Events"
        parser.add_argument(
            "-n",
            "--number",  # das hier steht in den kwargs
            type=int,
            help="Number of Reports to be generated",
            required=True,
        )
        parser.epilog = "Usage example: python manage.py my_first_command -n 3"

    def handle(self, *args, **kwargs):
        """diese Methode muss überschrieben werden."""
        numbers = kwargs.get("number")
        print(f"übergebener Wert: {numbers}")

        all_events = Event.objects.all()
        for event in all_events:
            print(event.__dict__)
