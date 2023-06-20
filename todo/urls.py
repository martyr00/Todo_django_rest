from django.urls import path
from .views import TodoCardAPIRetrieveUpdateDestroy, TodoCardAPIListCreate

app_name = 'todo'

urlpatterns = [
    path('', TodoCardAPIListCreate.as_view()),
    path('<int:pk>/', TodoCardAPIRetrieveUpdateDestroy.as_view()),
]
