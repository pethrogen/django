from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.http import Http404
from django.http import HttpResponse
from .models import Category, Event
from .forms import CategoryForm, EventForm


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy("events:categories")


class EventCreateView(CreateView):
    # event_form.html
    model = Event
    form_class = EventForm
    success_url = reverse_lazy("events:events")


def category_create(request):
    """
    neues Category anlegen
    events/category/create
    """
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("events:categories")

    else:
        # hier soll leeres Formular erzeugt werden
        form = CategoryForm()

    return render(request, "events/category_form.html", {"form": form})


def events(request):
    """
    events/

    """
    events = Event.objects.select_related("category", "author").all()
    return render(request, "events/events.html", {"events": events})


def event_detail(request, pk):
    """
    Dank Platzhalter in events/urls.py steht mir pk als Funktionsparameter
    zur Verfüfung.
    """
    # try:
    #     event = Event.objects.get(pk=pk)
    # except Event.DoesNotExist:
    #     raise Http404("sorry")
    event = get_object_or_404(Event, pk=pk)
    return render(request, "events/event_detail.html", {"event": event})


def categories(request):
    """
    events/categories
    """
    categories = Category.objects.all()
    return render(request, "events/categories.html", {"categories": categories})


def show(request) -> HttpResponse:
    """analysiere Request Objekt"""
    print(request.META)
    print("GET VALUES:", request.GET)
    if "id" in request.GET:
        print("ID:", request.GET["id"])
    print("USER: ", request.user)
    print("METHOD:", request.method)
    return HttpResponse("<h1>show</h1>")


def hello_world(request) -> HttpResponse:
    """
    jede View bekommt ein request-Objekt übergeben und
    muss ein HTTPResponse-Objekt zurückgeben.
    Aussnahme: eine Exception wird ausgelöst
    """
    return HttpResponse("hello world")
