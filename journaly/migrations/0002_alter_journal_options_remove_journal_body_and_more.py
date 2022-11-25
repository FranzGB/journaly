# Generated by Django 4.1.3 on 2022-11-25 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("journaly", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="journal",
            options={"ordering": ["date_modified"]},
        ),
        migrations.RemoveField(
            model_name="journal",
            name="body",
        ),
        migrations.RemoveField(
            model_name="journal",
            name="date",
        ),
        migrations.AddField(
            model_name="journal",
            name="content_description",
            field=models.TextField(default="A generic journal", max_length=400),
        ),
        migrations.AddField(
            model_name="journal",
            name="date_modified",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
