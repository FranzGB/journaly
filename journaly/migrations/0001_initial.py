# Generated by Django 4.1.3 on 2022-11-25 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Journal",
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
                ("title", models.CharField(max_length=100)),
                ("body", models.TextField()),
                ("date", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "ordering": ["date"],
            },
        ),
    ]