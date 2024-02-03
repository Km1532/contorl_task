from django.contrib.auth.models import User
from django.db import models
class Task(models.Model):
    STATUS_CHOICES = (
        ('в процесі', 'В процесі'),
        ('виконано', 'Виконано'),
        ('відкладено', 'Відкладено'),
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='в процесі')
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_tasks', null=True, blank=True)
    def __str__(self):
        return self.title
