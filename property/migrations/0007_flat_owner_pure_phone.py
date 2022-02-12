# Generated by Django 2.2.24 on 2022-02-12 08:28

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ("property", "0006_flat_liked_by"),
    ]

    operations = [
        migrations.AddField(
            model_name="flat",
            name="owner_pure_phone",
            field=phonenumber_field.modelfields.PhoneNumberField(
                blank=True,
                max_length=128,
                region=None,
                verbose_name="Номализованный номер владельца",
            ),
        ),
    ]