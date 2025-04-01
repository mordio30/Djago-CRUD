from django.db import models
from task_app.models import Task, TaskTemplate

# Create your models here.

class Subtask(TaskTemplate):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='subtasks')

    