from rest_framework import serializers

from todo.models import TodoCard


class TodoCardSerializer(serializers.ModelSerializer):
    """Serializer for todo_cards"""
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    user_id = serializers.CharField(read_only=True)

    class Meta:
        model = TodoCard
        fields = '__all__'
