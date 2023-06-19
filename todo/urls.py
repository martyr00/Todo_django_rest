from tastypie.api import Api
from django.urls import path, include

import todo
from todo.models import TodoCardResource

api = Api(api_name='v1')
api.register(TodoCardResource())

urlpatterns = [
    path('', include(api.urls), name='index')
]
