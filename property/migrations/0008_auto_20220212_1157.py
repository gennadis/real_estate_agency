# Generated by Django 2.2.24 on 2022-02-12 08:32
import phonenumbers
from django.db import migrations


def normalize_phone_number(apps, schema_editor):
    Flat = apps.get_model("property", "Flat")

    for flat in Flat.objects.all():
        parsed_phone = phonenumbers.parse(flat.owners_phonenumber, "RU")

        if phonenumbers.is_valid_number(parsed_phone):
            flat.owner_pure_phone = parsed_phone
            flat.save()


class Migration(migrations.Migration):
    dependencies = [
        ("property", "0007_flat_owner_pure_phone"),
    ]

    operations = [
        migrations.RunPython(normalize_phone_number),
    ]
