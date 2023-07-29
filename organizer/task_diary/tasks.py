from datetime import datetime,timedelta
from celery import shared_task
from django.core.mail import send_mail
from .models import Tasks


@shared_task
def send_mail_func(email):
    tasks=Tasks.objects.all()
    ourdelta=timedelta(hours=3)
    for task in tasks:
        if task.datecompleted == datetime.today()+ourdelta:
            subject = 'Информация о статусе задания '
            message = 'Срок исполнения Вашего задания истекает сегодня'
            send_mail(
                subject=subject,
                message=message,
                from_email='yadro@gmail.com',
                recipient_list=[email],
                fail_silently=False,
            )

    return 'Task was completed  successfully'

