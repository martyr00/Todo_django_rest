from .models import TodoCard
from rest_framework import generics

from .models import TodoCard
from .permission import IsOwnerOrAdmin
from .serializers import TodoCardSerializer


class TodoCardAPIListCreate(generics.ListCreateAPIView):
    queryset = TodoCard.objects.all()
    serializer_class = TodoCardSerializer
    permission_classes = (IsOwnerOrAdmin, )

    def get_queryset(self):
        query_set = super().get_queryset()
        user_from_db = User.objects.get(username=self.request.user)

        if user_from_db.is_superuser:
            return query_set
        return query_set.filter(user=self.request.user)


class TodoCardAPIRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoCard.objects.all()
    serializer_class = TodoCardSerializer
    permission_classes = (IsOwnerOrAdmin, )