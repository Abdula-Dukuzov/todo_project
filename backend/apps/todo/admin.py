from django.contrib import admin
from .models import Task, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "user")


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "category", "created_at", "due_date")
    list_filter = ("category",)
