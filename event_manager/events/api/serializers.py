"""
Serializer wandeln
- eigenende JSON Code in Pythonobjekte 
- ausgehende Pyhtonobjekte in JSON

"""
from rest_framework import serializers
from events import models


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Event
        fields = ("author", "name", "sub_title", "category", "date", "min_group")

        # extra informationen für felder angeben (hier: read_only)
        extra_kwargs = {"author": {"read_only": True}}


class EventInlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Event
        fields = ("author", "id", "name")


class CategorySerializer(serializers.ModelSerializer):
    # nested Serializers für die Darstellung der Events jeder Kategorie
    events = EventInlineSerializer(many=True, read_only=True)

    class Meta:
        model = models.Category
        fields = ("id", "name", "sub_title", "events")
