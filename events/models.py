from django.db import models

# Create your models here.

class Event(models.Model):
    event = models.CharField(max_length=50, unique = True)
    category = models.CharField(max_length=85,null=True, blank=True)
    date = models.DateField()



    def __str__(self) -> str:
        return self.event
