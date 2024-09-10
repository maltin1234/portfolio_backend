from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    # Display the user field in the list view
    list_display = ('title', 'project_description', 'created', 'completed', 'user')
    
    # Enable filtering by user in the admin
    list_filter = ('user',)

    # Search functionality for the user field
    search_fields = ('user__username',)

# Register the model with the admin site
admin.site.register(Todo, TodoAdmin)
