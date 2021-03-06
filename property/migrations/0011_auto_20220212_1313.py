# Generated by Django 2.2.24 on 2022-02-12 10:13

from django.db import migrations


def populate_owners_flats(apps, schema_editor):
    Flat = apps.get_model("property", "Flat")
    Owner = apps.get_model("property", "Owner")

    for owner in Owner.objects.all():
        owned_flats = Flat.objects.filter(owner=owner.fullname)
        owner.flats_owned.set(owned_flats)


class Migration(migrations.Migration):

    dependencies = [
        ("property", "0010_auto_20220212_1238"),
    ]

    operations = [migrations.RunPython(populate_owners_flats)]
