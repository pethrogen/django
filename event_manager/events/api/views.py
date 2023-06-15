"""
Viewset: beinhaltet alle API-Endpunkte automatisch
"""
from rest_framework import viewsets, permissions, authentication
from events import models

from . import serializers
from . import permissions


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EventSerializer
    queryset = models.Event.objects.all()
    permission_classes = [permissions.IsAdminUserOrReadOnly]
    authentication_classes = [authentication.TokenAuthentication]

    def perform_create(self, serializer):
        """Wird aufgerufen, bevor das Objekt angelegt wird."""
        author = self.request.user
        serializer.save(author=author)


class CategoryViewSet(viewsets.ModelViewSet):
    """
    get, post, patch, put
    """

    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()
