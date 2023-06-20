from django.urls import path
from .views import TodoCardAPIRetrieveUpdateDestroy, TodoCardAPIListCreate

app_name = 'todo'

urlpatterns = [
    path('todo/', TodoCardAPIListCreate.as_view()),
    path('todo/<int:pk>/', TodoCardAPIRetrieveUpdateDestroy.as_view()),
]