from django.db import models
from django.contrib.auth.models import User




class Project(models.Model):
    """A project the user is working on."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text


class Task(models.Model):
    """A task of a project to complete."""
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(default='', max_length=100, blank=True)
    text = models.TextField(blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_due = models.DateTimeField(auto_now_add=True)
    PRIORITY = [
        (0, "Critical"),
        (1, "Important"),
        (2, "Normal"),
        (3, "Low"),
    ]
    priority = models.IntegerField(choices=PRIORITY, default=2)

    class Meta:
        verbose_name_plural = 'tasks'

    def __str__(self):
        """Return a string representation of the model."""
        if(len(self.text) < 50 ):
            return f"{self.title} | {self.text}"
        else:
            return f"{self.title} | {self.text[:50]}..."