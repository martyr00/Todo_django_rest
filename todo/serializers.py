from rest_framework import serializers

from todo.models import TodoCard


class TodoCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoCard
        fields = '__all__'
