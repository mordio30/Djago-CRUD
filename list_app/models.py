from django.db import models

# Create your models here.
from django.db import models
from user_app.models import App_user

# Create your models here.

class BaseTemplate(models.Model): # this is a base template that we can inherit from
    name = models.CharField()
    completed = models.BooleanField(default=False)

    class Meta:
        abstract = True # abstract = true means jango will not create a database for this table. Other models can inherit from it, reusing its fields and methods.It acts as a base class for child models.
    
class List(BaseTemplate):
    user = models.ForeignKey(App_user, on_delete=models.CASCADE, related_name='lists')
    