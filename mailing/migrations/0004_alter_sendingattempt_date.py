# Generated by Django 5.1.4 on 2025-02-01 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mailing", "0003_alter_mailing_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sendingattempt",
            name="date",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
