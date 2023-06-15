from rest_framework import routers
from . import views

# Default Router erstellt alle URLs für diesen Endpunkt
router = routers.DefaultRouter()
router.register("category", views.CategoryViewSet)
router.register("event", views.EventViewSet)
