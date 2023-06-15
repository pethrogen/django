from django.shortcuts import render


def index(request):
    # liefert die React App aus
    return render(request, "frontend/build/index.html")
