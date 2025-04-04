# Generated by Django 5.1.4 on 2025-01-27 12:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Message",
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
                (
                    "message_subject",
                    models.CharField(
                        help_text="Введите тему письма.",
                        max_length=250,
                        verbose_name="Тема письма",
                    ),
                ),
                (
                    "message_body",
                    models.TextField(
                        help_text="Введите текст письма.", verbose_name="Текст письма"
                    ),
                ),
            ],
            options={
                "verbose_name": "Письмо",
                "verbose_name_plural": "Письма",
                "ordering": ["message_subject"],
            },
        ),
        migrations.CreateModel(
            name="Recipient",
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
                (
                    "email",
                    models.EmailField(
                        help_text="Введите адрес электронной почты.",
                        max_length=100,
                        unique=True,
                        verbose_name="Email",
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        help_text="Фамилия", max_length=100, verbose_name="Фамилия"
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        help_text="Имя", max_length=100, verbose_name="Имя"
                    ),
                ),
                (
                    "patronymic",
                    models.CharField(
                        blank=True,
                        help_text="Отчество (необязательно)",
                        max_length=100,
                        null=True,
                        verbose_name="Отчество",
                    ),
                ),
                (
                    "comment",
                    models.TextField(
                        blank=True,
                        help_text="Введите комментарий (необязательно)",
                        null=True,
                        verbose_name="Комментарий",
                    ),
                ),
            ],
            options={
                "verbose_name": "Получатель рассылки",
                "verbose_name_plural": "Получатели рассылки",
                "ordering": ["last_name"],
            },
        ),
        migrations.CreateModel(
            name="Mailing",
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
                (
                    "name",
                    models.CharField(
                        help_text="Введите название рассылки для удобного поиска",
                        max_length=100,
                        verbose_name="Название рассылки",
                    ),
                ),
                ("start_send", models.DateTimeField(default=None)),
                ("stop_send", models.DateTimeField(default=None)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("created", "Создана"),
                            ("processing", "Запущена"),
                            ("completed", "Завершена"),
                        ],
                        default="created",
                        max_length=20,
                        verbose_name="Статус рассылки",
                    ),
                ),
                (
                    "message",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="messages",
                        to="mailing.message",
                    ),
                ),
                (
                    "recipient",
                    models.ManyToManyField(
                        related_name="recipients", to="mailing.recipient"
                    ),
                ),
            ],
            options={
                "verbose_name": "Рассылка",
                "verbose_name_plural": "Рассылки",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="SendingAttempt",
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
                ("date", models.DateTimeField(default=None)),
                (
                    "status",
                    models.CharField(
                        choices=[("success", "Успешно"), ("fail", "Не успешно")],
                        max_length=20,
                    ),
                ),
                ("mail_server_response", models.TextField(blank=True, null=True)),
                (
                    "mailing",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mailing.mailing",
                    ),
                ),
            ],
        ),
    ]
