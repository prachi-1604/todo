from djongo import models

# Create your models here.
class Todo(models.Model):
    title=models.CharField(max_length=300)
    description=models.TextField()
    completed=models.BooleanField(default=False)
    
    # def __str(self) -> str:
    #     return self.title
    
    