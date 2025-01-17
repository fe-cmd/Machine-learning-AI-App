# Generated by Django 4.1 on 2022-09-07 06:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Data",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, null=True)),
                (
                    "age",
                    models.PositiveIntegerField(
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(5),
                            django.core.validators.MaxValueValidator(65),
                        ],
                    ),
                ),
                ("height", models.PositiveIntegerField(null=True)),
                (
                    "sex",
                    models.PositiveIntegerField(
                        choices=[(0, "Female"), (1, "Male")], null=True
                    ),
                ),
                ("predictions", models.CharField(blank=True, max_length=100)),
                ("date", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "ordering": ["-date"],
            },
        ),
    ]
