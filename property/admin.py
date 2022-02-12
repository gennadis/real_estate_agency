from django.contrib import admin

from .models import Flat, Claim, Owner


class OwnerInline(admin.TabularInline):
    model = Owner.flats_owned.through
    raw_id_fields = ("owner",)


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
    )
    list_editable = ("is_new_building",)
    list_filter = ("is_new_building", "rooms_number", "has_balcony")
    raw_id_fields = ("liked_by",)
    inlines = (OwnerInline,)


@admin.register(Claim)
class ClaimAdmin(admin.ModelAdmin):
    raw_id_fields = ("author", "flat")


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ("flats_owned",)
