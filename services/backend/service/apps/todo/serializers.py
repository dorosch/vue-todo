from django.db import transaction
from rest_framework import serializers

from apps.todo import models as todo_models


class TodoItemSerializer(serializers.ModelSerializer):
    list = serializers.PrimaryKeyRelatedField(
        required=True,
        queryset=todo_models.TodoList.objects
    )

    class Meta:
        model = todo_models.TodoItem
        fields = (
            'id',
            'text',
            'list'
        )
        read_only = (
            'id',
        )


class TodoListSerializer(serializers.ModelSerializer):
    items = TodoItemSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = todo_models.TodoList
        fields = (
            'id',
            'title',
            'items'
        )
        read_only = (
            'id',
        )

    @transaction.atomic
    def create(self, validated_data):
        items = validated_data.pop('items', [])
        instance = super().create(validated_data)
        todo_models.TodoItem.objects.bulk_create(
            [
                todo_models.TodoItem(list=instance, **item) for item in items
            ],
            batch_size=256
        )
        return instance
