from myapp.models import ToDoItem
from myapp.serializers import ToDoItemSerializer
from rest_framework import generics

class ToDoItemListCreate(generics.ListCreateAPIView):
	queryset = ToDoItem.objects.all()
	serializer_class = ToDoItemSerializer