from django.db import models

# Create your models here.
class ToDoItem(models.Model):
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=1000)
	completed = models.BooleanField()
	created_at = models.DateTimeField(auto_now_add=True)
