from celery import shared_task
from django.utils import timezone
from .models import Task


@shared_task
def notify_due_tasks():
    now = timezone.now()
    tasks = Task.objects.filter(
        due_date__lte=now,
        is_completed=False,
    )

    for task in tasks:
        print(
            f"[NOTIFY] Task '{task.title}' "
            f"for user {task.user.username} is due!"
        )
