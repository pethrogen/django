from django.contrib import admin
from .models import Category, Event


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "sub_title")  # wird angezeigt in Übersicht
    list_display_links = ("pk", "name")  # das sind die anklickbaren Spaltennamen


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "name",
        "sub_title",
        "author",
        "category",
        "get_category_subtitle",
        "is_active",
    )  # wird angezeigt in Übersicht
    list_display_links = ("pk", "name")  # das sind die anklickbaren Spaltennamen
    list_filter = ("category", "author")
    actions = ["make_active", "make_inactive"]

    @admin.action(description="Setze Events auf aktiv")
    def make_active(self, request, queryset):
        # queryset ist die Menge aller angeklickten Events
        queryset.update(is_active=True)

    @admin.action(description="Setze Events auf inaktiv")
    def make_inactive(self, request, queryset):
        queryset.update(is_active=False)

    @admin.display(description="Kategorie Subtitle")
    def get_category_subtitle(self, event):
        """Subtitle jeder Kategorie (event ist das aktuelle Event-Objekt)"""
        return event.category.sub_title


# admin.site.register(Category)
