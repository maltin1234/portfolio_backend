from django.db import models
from django.contrib.postgres.fields import ArrayField
# from users.models import CustomUser
from users.models import NewUser
from django.conf import settings


class Todo(models.Model):
    title = models.CharField(max_length=100)
    project_description = models.CharField(max_length=600)
    created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    link_url =  models.CharField(max_length=600)
    github_url = models.CharField(max_length=600)
    tags = ArrayField(
        models.CharField(
            models.CharField(max_length=5, blank=True),
       

        ),
    
    )
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
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE, related_name="todos")
    # "CustomUser"
    
    def __str__(self):
        return self.title
