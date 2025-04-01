from django.db import models
from list_app.models import List, BaseTemplate

# Create your models here.

class TaskTemplate(BaseTemplate): # this is a task template that we can inherit from.  it inherits the base template
    description = models.TextField()

    class Meta:
        abstract = True # abstract = true means jango will not create a database for this table. Other models can inherit from it, reusing its fields and methods.It acts as a base class for child models.
    
class Task(TaskTemplate):
    user = models.ForeignKey(List, on_delete=models.CASCADE, related_name='tasks')
