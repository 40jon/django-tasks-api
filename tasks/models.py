from django.db import models
from django.utils import timezone

class Task(models.Model):
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(null=True, blank=True)

    @property
    def is_overdue(self):
        if self.due_date and not self.completed:
            return self.due_date < timezone.now().date()
        return False
