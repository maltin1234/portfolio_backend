from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User



class Todo(models.Model):
    title = models.CharField(max_length=100)
    project_description = models.CharField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    '''
    category = ArrayField(
        ArrayField(
            models.CharField(max_length=10, blank=True),
            size=8,
        ),
        size=8,
    )
    '''
    image = models.ImageField(upload_to='images/')
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title
