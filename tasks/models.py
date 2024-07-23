from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    description = models.TextField()
    due_date=models.DateTimeField(null=True,blank=True)
    priority=models.CharField(max_length=50,choices=[('low','Low'),('medium','Medium'),('high','High')])
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)