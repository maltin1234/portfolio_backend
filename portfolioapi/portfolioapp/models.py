from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    category = ArrayField(
        ArrayField(
            models.CharField(max_length=10, blank=True),
            size=8,
        ),
     size=8,
    )
    image = models.ImageField(upload_to='images')