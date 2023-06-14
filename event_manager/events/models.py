from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()  # bezieht immer das aktuelle Usermodel

# from event_manager.mixins import DateMixin


class DateMixin(models.Model):
    # lege beim Erstellen den aktuellen Zeitstempel an
    created_at = models.DateTimeField(auto_now_add=True)
    # setze Zeitstempel wenn das Model aktualisiert wird
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(DateMixin):
    """Jedes Model muss von models.Model erben. Aus einem Model kann man
    eine DB-Tabelle erstellen oder ein Formular rendern lassen."""

    class Meta:
        verbose_name_plural = "Categories"
        verbose_name = "Category"
        # db_table = "cats"  # alternativer Tabellenname

    name = models.CharField(max_length=100)  # VARCHAR 100
    sub_title = models.CharField(max_length=200, null=True, blank=True)

    # null=darf in der DB null sein. blank=darf im Formular leer sein.
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        """String Repräsentation des Category Objects"""
        return self.name


class Event(DateMixin):
    """ein Event in der Zukunft, zb. Tennis im Stadtpark."""

    class GroupSize(models.IntegerChoices):
        """Enum mit Gruppengrössen"""

        SMALL = 5, "kleine Gruppe"
        BIG = 10, "mittelgrosse Gruppe"
        LARGE = 20, "sehr große Gruppe"
        UNLIMITED = 0, "ohne Begrenzung"

    name = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField()
    min_group = models.PositiveIntegerField(choices=GroupSize.choices)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="events"
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="events")
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name
