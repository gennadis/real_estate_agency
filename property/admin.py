from django.contrib import admin

from .models import Flat, Claim


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ("town", "address")
    readonly_fields = ("created_at",)
    list_display = (
        "address",
        "price",
        "is_new_building",
        "construction_year",
        "town",
        "owners_phonenumber",
        "owner_pure_phone",
    )
    list_editable = ("is_new_building",)
    list_filter = ("is_new_building", "rooms_number", "has_balcony")
    raw_id_fields = ("liked_by",)


@admin.register(Claim)
class ClaimAdmin(admin.ModelAdmin):
    raw_id_fields = ("author", "flat")
