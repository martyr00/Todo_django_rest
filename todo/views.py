from .models import TodoCard
from .serializers import TodoCardSerializer
from rest_framework import generics


class TodoCardAPIListCreate(generics.ListCreateAPIView):
    queryset = TodoCard.objects.all()
    serializer_class = TodoCardSerializer


class TodoCardAPIRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoCard.objects.all()
    serializer_class = TodoCardSerializer

