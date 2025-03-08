from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Project


# Register the model with the admin site
admin.site.register(Project)
