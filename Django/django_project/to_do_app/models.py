from django.db import models

# Create your models here.

# This is a model class, which is a subclass of django.db.models.Model
class to_do(models.Model):
    title = models.TextField()# This is a field of the model
    description = models.TextField()

    def __str__(self): # This is a string representation of the model object(title of the to_do object)
        return self.title
    
    class Meta():
        verbose_name = 'To Do'
        verbose_name_plural = 'To Dos'