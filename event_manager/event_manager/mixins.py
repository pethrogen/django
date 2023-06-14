from django.db import models

class DateMixin(models.Model):
    """Beispiel für ein projektweites Mixin"""
    # lege beim Erstellen den aktuellen Zeitstempel an
    created_at = models.DateTimeField(auto_now_add=True)
    # setze Zeitstempel wenn das Model aktualisiert wird
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True