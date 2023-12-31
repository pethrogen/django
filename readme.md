# Project Event Manager
Django Trainings Project

## Env-Datei anlegen
Auf Basis der env.exampe eine .env-Datei am gleichen Ort anlegen
und mit entsprechenden Daten füllen.

## Projekt starten
    python -m venv .envs/eventenv
    .envs/eventenv/Scripts/activate
    (eventenv) pip install pip-tools
    (eventenv) pip-sync requirements.txt requirements-dev.txt
    (eventenv) python manage.py runserver

## Pad (30 days valid)
- https://yopad.eu/p/djangodev
- https://yopad.eu/p/reactschulung

## Cors Header
Frontend auf anderem Server wie Backend
### cors installieren

    pip install django-cors-headers

in settings eintragen (vor common mittleware)

    "corsheaders.middleware.CorsMiddleware",  # wichtig, vor common

    INSTALLED_APPS = [
        ...
        "frontend",
        "corsheaders",
    ]

    CORS_ALLOWED_ORIGINS = ["example.com"]

## Docs
- Tutorial: https://djangoheroes.spielprinzip.com
- Django Docs: https://docs.djangoproject.com
- Pip-tools: https://github.com/jazzband/pip-tools
- Pip-tools: https://dida.do/de/blog/mehrschichtige-requirements-mit-pip-tools-verwalten

## LDAP
- https://django-auth-ldap.readthedocs.io/en/latest/reference.html

### gutes Einsteigertutorial
- https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Tutorial_local_library_website

## IIS (wfastcgi) Django Installation Tutorias

- https://nitinnain.com/setting-up-and-running-django-on-windows-iis-server/
- https://learn.microsoft.com/de-de/visualstudio/python/configure-web-apps-for-iis-windows?view=vs-2022
- https://medium.com/@Jonny_Waffles/deploy-django-on-iis-def658beae92

### Tag 1: Übersicht aller Manager Methoden
- https://docs.djangoproject.com/en/4.2/ref/models/querysets/#get


### Tag 2: Python Decorators
- https://realpython.com/primer-on-python-decorators/
- https://realpython.com/command-line-interfaces-python-argparse/
- https://docs.djangoproject.com/en/4.0/howto/static-files/deployment/

### Tag 3
- https://whitenoise.readthedocs.io/en/latest/
- https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing
- https://modwsgi.readthedocs.io/en/master/
- https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/modwsgi/

### Tag 4
- https://swagger.io/specification/
- https://drf-spectacular.readthedocs.io/en/latest/
- https://djangoheroes.spielprinzip.com/webapi/restful_api.html
