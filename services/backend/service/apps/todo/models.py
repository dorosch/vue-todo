from django.db import models


class TodoList(models.Model):
    title = models.CharField(
        max_length=64
    )


class TodoItem(models.Model):
    list = models.ForeignKey(
        to=TodoList,
        on_delete=models.CASCADE,
        related_name='items',
        related_query_name='item'
    )

    text = models.CharField(
        max_length=256
    )
