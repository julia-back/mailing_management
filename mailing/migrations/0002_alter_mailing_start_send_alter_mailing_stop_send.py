# Generated by Django 5.1.4 on 2025-01-31 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mailing", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mailing",
            name="start_send",
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name="mailing",
            name="stop_send",
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
