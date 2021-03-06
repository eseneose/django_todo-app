from django.db import models
from django.utils import timezone

class Todo(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return '%s: %s' % (self.id, self.title)

