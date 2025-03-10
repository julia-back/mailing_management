# Generated by Django 5.1.4 on 2025-02-02 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mailing", "0005_mailing_owner_message_owner_recipient_owner_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="mailing",
            options={
                "ordering": ["name"],
                "permissions": [("can_stop_mailing", "Can stop mailing")],
                "verbose_name": "Рассылка",
                "verbose_name_plural": "Рассылки",
            },
        ),
    ]
