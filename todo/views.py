from django.db.models import Prefetch
from django.http import HttpResponse
from rest_framework.response import Response

from .models import TodoCard
from .permission import IsOwnerOrAdmin
from .serializers import TodoCardSerializer
from rest_framework import viewsets, generics


# class TodoCardViewSet(viewsets.ModelViewSet):
#     queryset = TodoCard.objects.all()
#     serializer_class = TodoCardSerializer
#
#     def get_queryset(self):
#         pk = self.kwargs.get('pk')
#
#         if not pk:
#             return TodoCard.objects.all()
#
#         return TodoCard.objects.filter(pk=pk)


class TodoCardAPIListCreate(generics.ListCreateAPIView):
    queryset = TodoCard.objects.all()
    serializer_class = TodoCardSerializer
    permission_classes = (IsOwnerOrAdmin, )

    def get_queryset(self):
        query_set = super().get_queryset()
        return query_set.filter(user=self.request.user)


class TodoCardAPIRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoCard.objects.all()
    serializer_class = TodoCardSerializer
    permission_classes = (IsOwnerOrAdmin, )

