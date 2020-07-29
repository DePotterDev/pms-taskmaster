from django.db import models

# Create your models here.
class Project(models.Model):
    """A project the user is working on."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text


class Task(models.Model):
    """A task of a project to complete."""
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'tasks'

    def __str__(self):
        """Return a string representation of the model."""
        if(len(self.text) < 50 ):
            return f"{self.text}"
        else:
            return f"{self.text[:50]}..."