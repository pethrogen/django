"""
PROJEKT URLs
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from drf_spectacular.views import SpectacularAPIView
from drf_spectacular.views import SpectacularSwaggerView
from rest_framework.authtoken.views import obtain_auth_token
from events.api.urls import router

urlpatterns = [
    path("", include("frontend.urls")),
    path("admin/", admin.site.urls),
    path("events/", include("events.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("token", obtain_auth_token, name="token"),  # hier den token holen
    path("api/", include(router.urls)),
    path(
        "schema/",
        SpectacularAPIView.as_view(api_version="v2"),
        name="schema",
    ),
    path(
        "docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
