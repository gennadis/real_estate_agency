# Generated by Django 2.2.24 on 2022-02-12 09:27

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ("property", "0008_auto_20220212_1157"),
    ]

    operations = [
        migrations.CreateModel(
            name="Owner",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "fullname",
                    models.CharField(
                        max_length=200, verbose_name="ФИО владельца", db_index=True
                    ),
                ),
                (
                    "phonenumber",
                    models.CharField(
                        max_length=20, verbose_name="Номер владельца", db_index=True
                    ),
                ),
                (
                    "pure_phone",
                    phonenumber_field.modelfields.PhoneNumberField(
                        blank=True,
                        max_length=128,
                        null=True,
                        region=None,
                        verbose_name="Номализованный номер владельца",
                        db_index=True,
                    ),
                ),
                (
                    "flats_owned",
                    models.ManyToManyField(
                        related_name="owners",
                        to="property.Flat",
                        verbose_name="Квартиры в собственности",
                        db_index=True,
                    ),
                ),
            ],
        ),
    ]
