from django import forms
from django.core.exceptions import ValidationError
from .models import Event, Category


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        # fields = "__all__"
        # fields = ("name", "sub_title")
        exclude = ("author",)

        widgets = {
            "date": forms.DateInput(
                format=("%Y-%m-%d %H:%M"), attrs={"type": "datetime-local"}
            ),
        }

        labels = {
            "sub_title": "Genre",
        }

    def clean_sub_title(self):
        """
        ### asdsdaf ###
        d = {
            "a": 1
        }
        d["a"]
        d.get("a", "")

        """
        sub_title = self.cleaned_data["sub_title"]

        if isinstance(sub_title, str) and "@" in sub_title:
            raise ValidationError("im Subtitle darf kein @ sein")

        return sub_title


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
