from django.db import models
from django.conf import settings
from django.utils import timezone

from apps.common.utils import generate_hash_id


User = settings.AUTH_USER_MODEL


class Category(models.Model):
    id = models.CharField(
        primary_key=True,
        max_length=64,
        editable=False
    )
    name = models.CharField(max_length=100)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="categories"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = generate_hash_id(self.name, str(self.user))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Task(models.Model):
    id = models.CharField(
        primary_key=True,
        max_length=64,
        editable=False
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="tasks"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="tasks"
    )
    created_at = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField()
    is_completed = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = generate_hash_id(
                self.title,
                str(self.user),
                str(self.due_date)
            )
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
