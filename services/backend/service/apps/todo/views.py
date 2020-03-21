from rest_framework import generics as rest_framework_generics

from apps.todo import (
    models as todo_models,
    serializers as todo_serializers,
)


class TodoList(rest_framework_generics.ListCreateAPIView):
    serializer_class = todo_serializers.TodoListSerializer
    queryset = todo_models.TodoList.objects.prefetch_related('items')


class TodoListDetail(rest_framework_generics.RetrieveUpdateDestroyAPIView):
    serializer_class = todo_serializers.TodoListSerializer
    queryset = todo_models.TodoList.objects.prefetch_related('items')


class TodoItemList(rest_framework_generics.ListCreateAPIView):
    serializer_class = todo_serializers.TodoItemSerializer
    queryset = todo_models.TodoItem.objects.select_related('list')


class TodoItemDetail(rest_framework_generics.RetrieveUpdateDestroyAPIView):
    serializer_class = todo_serializers.TodoItemSerializer
    queryset = todo_models.TodoItem.objects.select_related('list')
