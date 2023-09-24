from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateTimeField()
    priority = models.CharField(max_length=10, choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')])
    is_completed = models.BooleanField(default=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_update_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photos = models.ManyToManyField('Photo', blank=True,related_name='tasks')

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['priority']

class Photo(models.Model):
    task = models.ForeignKey(Task, related_name='task_photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='task_photos/')

    def __str__(self):
        return str(self.image)