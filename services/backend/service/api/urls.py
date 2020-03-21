from django.urls import path
from django.urls import include

from apps.todo import views as todo_views

urlpatterns = [
    path('todo/', include([
        path('lists/', include([
            path('', todo_views.TodoList.as_view()),
            path('<int:pk>/', todo_views.TodoListDetail.as_view())
        ])),
        path('items/', include([
            path('', todo_views.TodoItemList.as_view()),
            path('<int:pk>/', todo_views.TodoItemDetail.as_view())
        ]))
    ]))
]
