from celery import shared_task
from django.core.mail import send_mail
import os

EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER", "")


@shared_task
def send_lead_emails(user_email, attorney_email, full_name):
    send_mail(
        'Arizangiz qabul qilindi',
        'Sizning arizangiz qabul qilindi, tez orada siz bilan bog‘lanamiz.',
        str(EMAIL_HOST_USER),
        [user_email],
    )
    send_mail(
        'Yangi ariza',
        f"Yangi ariza: {full_name}, Email: {user_email}",
        str(EMAIL_HOST_USER),
        [str(EMAIL_HOST_USER)],
    )
