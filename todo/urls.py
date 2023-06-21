from django.urls import path
from rest_framework import routers

from .views import TodoCardAPIListCreate, TodoCardAPIRetrieveUpdateDestroy

app_name = 'todo'

urlpatterns = [
    path('', TodoCardAPIListCreate.as_view()),
    path('<int:pk>/', TodoCardAPIRetrieveUpdateDestroy.as_view()),
]

