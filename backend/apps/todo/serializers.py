from rest_framework import serializers
from .models import Task, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name", "created_at")


class TaskSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Task
        fields = (
            "id",
            "title",
            "description",
            "category",
            "category_id",
            "due_date",
            "created_at",
            "is_completed",
        )
        read_only_fields = ("id", "created_at")

    def create(self, validated_data):
        category_id = validated_data.pop("category_id", None)
        user = self.context["request"].user

        task = Task.objects.create(user=user, **validated_data)

        if category_id:
            task.category_id = category_id
            task.save()

        return task
