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


class TaskSection(models.Model):
    """ Title of a group of tasks """
    project = models.ForeignKey(Project, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True, default='')
    desc = models.CharField(max_length=300, default='', blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """ Return a string representation of the model. """
        return self.title


class Task(models.Model):
    """ Will be the title/segment that will contain the task items """
    task_section = models.ForeignKey(TaskSection, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default='')
    text = models.TextField(max_length=2000, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    PRIORITY = [
        (0, "Critical"),
        (1, "Important"),
        (2, "Normal"),
        (3, "Low"),
    ]
    priority = models.IntegerField(choices=PRIORITY, default=2, blank=True)
    comments = models.CharField(max_length=1000, default='', blank=True)

    class Meta:
        verbose_name_plural = 'tasks'

    def __str__(self):
        """ Return a string representation of the model. """
        """Return a string representation of the model."""
        if(len(self.text) < 50 ):
            return f"{self.title} | {self.text}"
        else:
            return f"{self.title} | {self.text[:50]}..."
