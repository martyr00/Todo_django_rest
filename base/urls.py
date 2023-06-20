from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('todo.urls')),
    # path('api/v1/todolist/', TodoCardAPIView.as_view()),
    # path('api/v1/todolist/<int:pk>/', TodoCardAPIView.as_view()),
]
