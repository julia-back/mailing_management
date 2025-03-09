from django.urls import path
from django.views.decorators.cache import cache_page

from . import views
from .apps import MailingConfig

app_name = MailingConfig.name

urlpatterns = [
    path("home/", cache_page(60 * 15)(views.HomeView.as_view()), name="home"),
    path("sending_attempt_list/", views.SendingAttemptListView.as_view(), name="sending_attempt_list"),

    path("recipient_list/", cache_page(60)(views.RecipientListView.as_view()), name="recipient_list"),
    path("recipient_detail/<int:pk>/", views.RecipientDetailView.as_view(), name="recipient_detail"),
    path("recipient_create/", views.RecipientCreateView.as_view(), name="recipient_create"),
    path("recipient_update/<int:pk>/", views.RecipientUpdateView.as_view(), name="recipient_update"),
    path("recipient_delete/<int:pk>/", views.RecipientDeleteView.as_view(), name="recipient_delete"),

    path("message_list/", cache_page(60)(views.MessageListView.as_view()), name="message_list"),
    path("message_detail/<int:pk>/", views.MessageDetailView.as_view(), name="message_detail"),
    path("message_create/", views.MessageCreateView.as_view(), name="message_create"),
    path("message_update/<int:pk>/", views.MessageUpdateView.as_view(), name="message_update"),
    path("message_delete/<int:pk>/", views.MessageDeleteView.as_view(), name="message_delete"),

    path("mailing_list/", cache_page(60)(views.MailingListView.as_view()), name="mailing_list"),
    path("mailing_detail/<int:pk>/", views.MailingDetailView.as_view(), name="mailing_detail"),
    path("mailing_create/", views.MailingCreateView.as_view(), name="mailing_create"),
    path("mailing_update/<int:pk>/", views.MailingUpdateView.as_view(), name="mailing_update"),
    path("mailing_delete/<int:pk>/", views.MailingDeleteView.as_view(), name="mailing_delete"),

    path("mailing_start/<int:pk>/", views.MailingStartView.as_view(), name="mailing_start"),
    path("mailing_stop/<int:pk>/", views.MailingStopView.as_view(), name="mailing_stop"),
]
