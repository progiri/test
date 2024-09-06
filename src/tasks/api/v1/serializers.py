from rest_framework import serializers
from tasks.models import Task


class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ("title", "description", "user")


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        exclude = ("user",)

