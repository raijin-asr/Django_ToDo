from django.db import models

# Create your models here.
class Task(models.Model):
    title= models.CharField(max_length=200)
    description= models.TextField(null=True, blank=True)
    due_date= models.DateTimeField()
    due_time= models.TimeField()
    is_completed= models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title} - {self.due_date} - {self.due_time} - {self.is_completed}'


