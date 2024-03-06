from django.db import models
from django.core.exceptions import ValidationError

class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20, blank=True)

    def clean(self):
        if not self.title and not self.description:
            raise ValidationError("Title and description cannot be blank.")

    def save(self, *args, **kwargs):
        self.full_clean()  # Run full_clean() before saving to validate the model
        super().save(*args, **kwargs)

    
    
    