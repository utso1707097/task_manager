from django.contrib import admin
from .models import Task , Photo
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'due_date', 'priority', 'is_completed', 'user')
    list_filter = ('priority', 'is_completed')
    search_fields = ('title', 'description', 'user__username') 

admin.site.register(Task, TaskAdmin)
admin.site.register(Photo)