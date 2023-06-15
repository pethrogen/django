# Frontend Application anlegen

## 1. Frontend anlegen

    python manage.py startapp frontend

- models.py löschen
- migrations/ löschen
- tests.py löschen

- urls.py anlegen
- templates/ anlegen

## 2. Verlinkungen
- in frontend/urls.py
- in event_manager/urls.py

## 2. Reacpt App erstellen

    cd frontend/template
    npx create-react-app frontend
    cd frontend
    npm run build


## 3. Static Files festlegen

    STATICFILES_DIRS = [
        BASE_DIR / "static",
        BASE_DIR / "frontend/templates/frontend/build/static",
    ]