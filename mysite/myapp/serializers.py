from rest_framework import serializers
from myapp.models import ToDoItem

class ToDoItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = ToDoItem
		fields = ('id', 'title', 'description', 'completed', 'created_at')