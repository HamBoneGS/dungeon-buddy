# Generated by Django 4.1.2 on 2022-10-30 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("notes", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="note",
            name="date_created",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
