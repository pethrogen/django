"""
URLs der App events

/events/hello
/events/show

Aufgabe
Route: /events/show
View show anlegen, die das Request-objekt ausgibt
mit print(dir(request))
Rückgabe: show

pfad-Funktion benötigt drei Argumente:
- Pfad-Anteil
- Funktionsreferenz
- Name des Pfades (muss nicht Funktionsname sein)

http://127.0.0.1:8000/events/event/2
"""
from django.urls import path
from . import views

# app_name um im Template auf die App zu referenziern
app_name = "events"

urlpatterns = [
    path("", views.events, name="events"),
    path("event/<int:pk>", views.event_detail, name="event_detail"),
    path("category/create", views.category_create, name="category_create"),
    # path("category/add", views.CategoryCreateView.as_view(), name="category_add"),
    path("event/create", views.EventCreateView.as_view(), name="event_create"),
    path("hello", views.hello_world, name="hello_world"),
    path("show", views.show, name="show"),
    path("categories", views.categories, name="categories"),
]
