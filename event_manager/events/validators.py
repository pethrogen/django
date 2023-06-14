from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils import timezone


@deconstructible
class BadWordFilter:
    def __init__(self, bad_word_list: list):
        self.bad_word_list = bad_word_list

    def __call__(self, current_field_value):
        for bad_word in self.bad_word_list:
            if bad_word in current_field_value:
                raise ValidationError(f"Dieses Wort ist böse: {bad_word}!")


def date_in_past(current_field_value) -> None:
    """Prüfe, ob Datum in der Vergangenheit liegt. Falls ja,
    erhebe ValidationError
    """
    if current_field_value < timezone.now():
        raise ValidationError("Datum darf nicht in der Vergangenheit liegen.")


class Test:
    # dundercall erlaubt das Aufrufen des Objekts wie eine Funktion
    def __call__(self, value):
        print(f"ich bin hier mit {value}")


test = Test()
test("hallo")
