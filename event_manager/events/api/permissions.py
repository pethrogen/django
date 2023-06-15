from rest_framework import permissions


class IsAdminUserOrReadOnly(permissions.IsAdminUser):
    """User muss admin sein, um zu schreiben. Lesen darf jeder."""

    def has_permission(self, request, view):
        # ist User Admin oder nicht?
        is_admin = super().has_permission(request, view)

        # SAFE_METHODS = GET, HEAD, OPTIONS
        # wenn methode in Safemethods, dann true
        # ansonsten is_admin ADMIN oder nicht
        return request.method in permissions.SAFE_METHODS or is_admin
