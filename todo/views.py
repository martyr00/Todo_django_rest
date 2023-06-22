from django.contrib.auth.models import User
from rest_framework import generics
from .models import TodoCard
from .permission import IsOwnerOrAdmin
from .serializers import TodoCardSerializer


class TodoCardAPIListCreate(generics.ListCreateAPIView):
    """class: GET list todo_cards for one_user and POST one todo_card from one user"""
    queryset = TodoCard.objects.all()
    serializer_class = TodoCardSerializer
    permission_classes = (IsOwnerOrAdmin, )

    def get_queryset(self):
        """Response all list todo_card of user or if user is superuser response all list"""
        query_set = super().get_queryset()
        user_from_db = User.objects.get(username=self.request.user)

        if user_from_db.is_superuser:
            return query_set
        return query_set.filter(user=self.request.user)


class TodoCardAPIRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """class: PUT, PATCH, DELETE, GET for one todo_card from one user"""
    queryset = TodoCard.objects.all()
    serializer_class = TodoCardSerializer
    permission_classes = (IsOwnerOrAdmin, )
