from django.db import models


class Recipient(models.Model):

    email = models.EmailField(max_length=100, unique=True,
                              verbose_name="Email",
                              help_text="Введите адрес электронной почты.")
    last_name = models.CharField(max_length=100,
                                 verbose_name="Фамилия",
                                 help_text="Фамилия")
    first_name = models.CharField(max_length=100,
                                  verbose_name="Имя",
                                  help_text="Имя")
    patronymic = models.CharField(max_length=100, null=True, blank=True,
                                  verbose_name="Отчество",
                                  help_text="Отчество (необязательно)")
    comment = models.TextField(null=True, blank=True,
                               verbose_name="Комментарий",
                               help_text="Введите комментарий (необязательно)")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Получатель рассылки"
        verbose_name_plural = "Получатели рассылки"
        ordering = ["last_name"]


class Message(models.Model):

    message_subject = models.CharField(max_length=250,
                                       verbose_name="Тема письма",
                                       help_text="Введите тему письма.")
    message_body = models.TextField(verbose_name="Текст письма",
                                    help_text="Введите текст письма.")

    def __str__(self):
        return self.message_subject

    class Meta:
        verbose_name = "Письмо"
        verbose_name_plural = "Письма"
        ordering = ["message_subject"]


class Mailing(models.Model):

    STATUS_MAILING_CHOICES = {"created": "Создана",
                              "processing": "Запущена",
                              "completed": "Завершена"}

    name = models.CharField(max_length=100,
                            verbose_name="Название рассылки",
                            help_text="Введите название рассылки для удобного поиска")
    start_send = models.DateTimeField(default=None, null=True, blank=True)
    stop_send = models.DateTimeField(default=None, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_MAILING_CHOICES, default="Создана",
                              verbose_name="Статус рассылки")
    message = models.ForeignKey(Message, on_delete=models.SET_NULL, null=True,
                                related_name="messages")
    recipient = models.ManyToManyField(Recipient, related_name="recipients")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"
        ordering = ["name"]


class SendingAttempt(models.Model):

    STATUS_ATTEMPT_CHOICES = {"success": "Успешно",
                              "fail": "Не успешно"}

    date = models.DateTimeField(default=None)
    status = models.CharField(max_length=20, choices=STATUS_ATTEMPT_CHOICES)
    mail_server_response = models.TextField(null=True, blank=True)
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE)
