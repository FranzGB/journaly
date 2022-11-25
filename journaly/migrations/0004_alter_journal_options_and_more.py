# Generated by Django 4.1.3 on 2022-11-25 01:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("journaly", "0003_journalentry"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="journal",
            options={"ordering": ["journal_title"]},
        ),
        migrations.RenameField(
            model_name="journal",
            old_name="title",
            new_name="journal_title",
        ),
        migrations.RemoveField(
            model_name="journal",
            name="date_modified",
        ),
    ]